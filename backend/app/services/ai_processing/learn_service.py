from app.database.schemas.learn import LearnResponse


class LearnService:
    def explain(self, topic: str) -> LearnResponse:
        cleaned = topic.strip() or "Artificial Intelligence"
        return LearnResponse(
            topic=cleaned,
            explanation=f"{cleaned} means software doing useful tasks that usually need human thinking, like understanding text, generating ideas, or making predictions.",
            why_it_matters="It helps people save time, automate work, and build smarter products.",
            steps=[
                "Start with the problem AI is trying to solve.",
                "See one beginner-friendly example.",
                "Try a free tool before learning advanced features.",
                "Use AI on a small real task so the concept feels practical.",
            ],
            examples=[
                "A student summarizing lessons with AI.",
                "A developer debugging code with AI help.",
                "A marketer creating draft content faster.",
            ],
            difficulty="Beginner",
        )

