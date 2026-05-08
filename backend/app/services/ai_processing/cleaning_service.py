class CleaningService:
    def clean_records(self, records: list[dict]) -> list[dict]:
        seen_urls: set[str] = set()
        cleaned: list[dict] = []
        for record in records:
            title = (record.get("title") or "").strip()
            source_url = (record.get("source_url") or "").strip()
            if not title or not source_url:
                continue
            if source_url in seen_urls:
                continue
            if any(flag in title.lower() for flag in ["404", "not found", "error"]):
                continue
            seen_urls.add(source_url)
            cleaned.append(
                {
                    **record,
                    "title": " ".join(title.split()),
                    "source_url": source_url,
                }
            )
        return cleaned

