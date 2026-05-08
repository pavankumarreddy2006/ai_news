from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.core.config.settings import get_settings
from app.database.session.engine import SessionLocal
from app.schedulers.cleanup_jobs.cleanup_job import run_cleanup_job
from app.schedulers.news_jobs.refresh_job import run_refresh_job
from app.schedulers.telegram_jobs.digest_job import run_telegram_job

settings = get_settings()
scheduler = AsyncIOScheduler()


def _job_wrapper(coro):
    async def runner():
        db = SessionLocal()
        try:
            await coro(db)
        finally:
            db.close()

    return runner


def start_scheduler() -> None:
    if not settings.enable_background_jobs or scheduler.running:
        return
    scheduler.add_job(_job_wrapper(run_refresh_job), "interval", minutes=settings.refresh_interval_minutes, id="refresh-news")
    scheduler.add_job(_job_wrapper(run_cleanup_job), "interval", hours=12, id="cleanup-news")
    scheduler.add_job(
        _job_wrapper(run_telegram_job),
        "cron",
        hour=settings.telegram_digest_hour,
        minute=settings.telegram_digest_minute,
        timezone=settings.telegram_digest_timezone,
        id="telegram-digest",
    )
    scheduler.start()


def stop_scheduler() -> None:
    if scheduler.running:
        scheduler.shutdown(wait=False)
