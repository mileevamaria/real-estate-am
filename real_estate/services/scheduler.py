from apscheduler.schedulers.blocking import BlockingScheduler

from real_estate.services import collect_apartments

scheduler = BlockingScheduler()

scheduler.add_job(
    collect_apartments,
    trigger='interval',
    hours=1,
    max_instances=1,
    coalesce=True,
)
