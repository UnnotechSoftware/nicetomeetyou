from celery import Celery


app = Celery('crawler')
app.config_from_object('crawler.celery_config')
