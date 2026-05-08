from app.core.config.settings import get_settings

settings = get_settings()


def build_source_registry() -> list[dict]:
    return [
        {"name": "OpenAI News", "kind": "rss", "source": "OpenAI", "url": settings.openai_rss, "category": "OpenAI", "content_type": "news"},
        {"name": "Anthropic News", "kind": "rss", "source": "Anthropic", "url": settings.anthropic_rss, "category": "LLMs", "content_type": "news"},
        {"name": "Google AI Blog", "kind": "rss", "source": "Google AI", "url": settings.google_ai_rss, "category": "AI Research", "content_type": "research"},
        {"name": "DeepMind Blog", "kind": "rss", "source": "DeepMind", "url": settings.deepmind_rss, "category": "LLMs", "content_type": "research"},
        {"name": "NVIDIA AI", "kind": "rss", "source": "NVIDIA", "url": settings.nvidia_ai_rss, "category": "AI Infrastructure", "content_type": "news"},
        {"name": "Hugging Face Blog", "kind": "rss", "source": "Hugging Face", "url": settings.huggingface_rss, "category": "AI Tools", "content_type": "tools"},
        {"name": "TechCrunch AI", "kind": "rss", "source": "TechCrunch", "url": settings.techcrunch_ai_rss, "category": "AI Startups", "content_type": "news"},
        {"name": "The Verge AI", "kind": "rss", "source": "The Verge", "url": settings.verge_ai_rss, "category": "AI News", "content_type": "news"},
        {"name": "GitHub Trending AI", "kind": "html", "source": "GitHub", "url": "https://github.com/trending/python?since=daily", "category": "Coding AI", "content_type": "repository"},
        {"name": "Product Hunt AI", "kind": "html", "source": "Product Hunt", "url": "https://www.producthunt.com/topics/artificial-intelligence", "category": "AI Launches", "content_type": "launch"},
        {"name": "Reddit AI", "kind": "html", "source": "Reddit", "url": "https://www.reddit.com/r/artificial/", "category": "AI Discussions", "content_type": "discussion"},
        {"name": "YouTube AI", "kind": "html", "source": "YouTube", "url": "https://www.youtube.com/results?search_query=AI+news", "category": "AI Tutorials", "content_type": "video"},
    ]


SOURCE_REGISTRY = build_source_registry()
