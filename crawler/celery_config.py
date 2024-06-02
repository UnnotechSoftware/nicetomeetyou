from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

broker_url = os.getenv('CELERY_BROKER_URL')
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
        'schedule': timedelta(minutes=15),
    }
}
