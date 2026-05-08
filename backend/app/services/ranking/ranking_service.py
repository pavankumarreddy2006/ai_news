from collections import Counter
from datetime import datetime, timezone


KEYWORD_WEIGHTS = {
    "openai": 2.0,
    "agent": 1.8,
    "workflow": 1.7,
    "coding": 1.8,
    "video": 1.5,
    "tutorial": 1.8,
    "free": 1.6,
    "launch": 1.6,
    "startup": 1.5,
    "llm": 1.7,
    "automation": 1.7,
    "tool": 1.5,
}


class RankingService:
    def score(self, payload: dict) -> dict:
        text = f"{payload.get('title', '')} {payload.get('summary', '')}".lower()
        keywords = self._keywords(text)
        keyword_score = sum(KEYWORD_WEIGHTS.get(keyword, 0) for keyword in keywords)
        age_hours = self._age_hours(payload.get("published_at"))
        freshness = max(0.5, 12 / age_hours)
        engagement = min(10.0, keyword_score * 2.4 + len(text.split()) / 16)
        virality = min(10.0, 2.0 + text.count("ai") + text.count("launch") + text.count("agent"))
        beginner = min(10.0, 3.0 + sum(token in text for token in ["simple", "free", "guide", "tool", "tutorial"]))
        trending = round((virality + freshness + engagement) / 3, 2)
        ranking = round((keyword_score * 3.2) + freshness + engagement + virality + beginner, 2)
        return {
            **payload,
            "keywords": ", ".join(keywords),
            "virality_score": round(virality, 2),
            "engagement_score": round(engagement, 2),
            "freshness_score": round(freshness, 2),
            "beginner_score": round(beginner, 2),
            "trending_score": trending,
            "ranking_score": ranking,
            "is_trending": ranking >= 16,
        }

    def _keywords(self, text: str) -> list[str]:
        tokens = [word.strip(".,!?;:()[]").lower() for word in text.split()]
        filtered = [word for word in tokens if len(word) > 3]
        return [word for word, _ in Counter(filtered).most_common(8)]

    def _age_hours(self, published_at: datetime | None) -> float:
        if isinstance(published_at, datetime):
            delta = datetime.now(timezone.utc) - published_at.astimezone(timezone.utc)
            return max(1.0, delta.total_seconds() / 3600)
        return 6.0

