from datetime import datetime, timezone

import feedparser
import httpx
from bs4 import BeautifulSoup

from app.core.config.settings import get_settings
from app.core.constants.sources import SOURCE_REGISTRY
from app.core.logging.logger import get_logger

settings = get_settings()
logger = get_logger(__name__)


class FeedCollector:
    def fetch_all(self) -> list[dict]:
        records: list[dict] = []
        for source in SOURCE_REGISTRY:
            try:
                if source["kind"] == "rss":
                    records.extend(self._fetch_rss(source))
                else:
                    records.extend(self._fetch_html(source))
            except Exception as exc:
                logger.warning("Collector failed for %s: %s", source["source"], exc)
        return records

    def _fetch_rss(self, source: dict) -> list[dict]:
        with httpx.Client(
            timeout=settings.request_timeout_seconds,
            headers={"User-Agent": "AI News Platform/1.0", "Accept": "application/rss+xml, application/xml, text/xml;q=0.9, */*;q=0.8"},
            follow_redirects=True,
        ) as client:
            response = client.get(source["url"])
            response.raise_for_status()
        feed = feedparser.parse(response.content)
        items: list[dict] = []
        for entry in feed.entries[: settings.max_news_items_per_source]:
            items.append(
                {
                    "title": entry.get("title", source["name"]),
                    "source": source["source"],
                    "source_url": entry.get("link", source["url"]),
                    "image_url": self._extract_image(entry),
                    "category": source["category"],
                    "content_type": source["content_type"],
                    "published_at": self._parse_date(entry),
                }
            )
        return items

    def _fetch_html(self, source: dict) -> list[dict]:
        with httpx.Client(timeout=settings.request_timeout_seconds, headers={"User-Agent": "AI News Platform"}) as client:
            response = client.get(source["url"])
            response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string.strip() if soup.title and soup.title.string else source["name"]
        return [
            {
                "title": title,
                "source": source["source"],
                "source_url": source["url"],
                "image_url": "",
                "category": source["category"],
                "content_type": source["content_type"],
                "published_at": datetime.now(timezone.utc),
            }
        ]

    def _extract_image(self, entry: dict) -> str:
        media = entry.get("media_content") or []
        if media:
            return media[0].get("url", "")
        return ""

    def _parse_date(self, entry: dict) -> datetime:
        if entry.get("published_parsed"):
            return datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
        return datetime.now(timezone.utc)
