from datetime import timedelta

broker_url = 'redis://cache:6379/0'
result_backend = 'db+sqlite:///db.sqlite3'
result_serializer = 'json'
result_expires = 60 * 60 * 24
timezone = 'Asia/Taipei'
imports = (
    'crawler.tasks',
)
beat_schedule = {
    'every-5-minutes': {
        'task': 'crawler.tasks.process',
        'schedule': timedelta(seconds=15),
    }
}
