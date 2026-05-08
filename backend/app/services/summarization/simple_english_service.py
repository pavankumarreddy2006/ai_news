class SimpleEnglishService:
    def enrich(self, title: str, source: str, category: str) -> dict:
        lower = title.lower()
        if any(token in lower for token in ["launch", "release", "ship"]):
            easy = "A new AI product, feature, or update is now available for people to explore."
            why = "It helps users try fresh AI capabilities earlier."
        elif any(token in lower for token in ["agent", "workflow", "automation"]):
            easy = "This update is about AI that can handle tasks or workflows with less manual effort."
            why = "It shows how AI is becoming more practical for everyday work."
        elif any(token in lower for token in ["video", "image", "creator"]):
            easy = "This AI helps people create, edit, or improve visual content faster."
            why = "It saves time for creators, teams, and beginners."
        elif any(token in lower for token in ["code", "developer", "github"]):
            easy = "This AI helps developers write, understand, or ship code more quickly."
            why = "It can make software work faster and easier to learn."
        else:
            easy = "This is an important AI update explained in a simple and beginner-friendly way."
            why = "It helps people keep up with how AI tools and trends are changing."

        return {
            "summary": f"{title} from {source} is part of the latest wave of AI news and product movement.",
            "easy_summary": easy,
            "why_it_matters": why,
            "who_should_use_it": "Students, creators, operators, founders, and developers",
            "beginner_explanation": f"In simple words, {easy.lower()}",
            "difficulty_level": "Intermediate" if category in {"LLMs"} else "Beginner",
            "reading_time": "3 min",
        }

