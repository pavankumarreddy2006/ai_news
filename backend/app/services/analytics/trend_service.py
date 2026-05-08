from app.database.models.trending_topic import TrendingTopic
from app.database.models.article import Article


class TrendService:
    def build_topics(self, articles: list[Article]) -> list[TrendingTopic]:
        scores: dict[str, float] = {}
        for article in articles[:20]:
            for keyword in [token.strip() for token in article.keywords.split(",") if token.strip()]:
                scores[keyword] = scores.get(keyword, 0) + 1.0
        return [
            TrendingTopic(
                topic=topic.title(),
                context=f"{topic.title()} is appearing across recent AI launches, tools, and tutorials.",
                score=round(score * 8.5, 2),
                velocity=round(score * 1.7, 2),
            )
            for topic, score in sorted(scores.items(), key=lambda pair: pair[1], reverse=True)[:10]
        ]

