from app.workers.scheduler import scheduler


def test_scheduler_object_exists():
    assert scheduler is not None

