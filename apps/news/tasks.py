from celery import chord
from celery.signals import task_postrun
from celery.utils.log import get_task_logger

from apps.news.base_task import custom_celery_task
from apps.news.models import News
from utils.client import NBANewsFetcher

logger = get_task_logger(__name__)
fetcher = NBANewsFetcher('http://tw-nba.udn.com/nba/index')  # noqa


@custom_celery_task(name='news_crawler', retry_backoff=5, max_retries=3)
def news_crawler():
    news_list = fetcher.get_latest_news_list('//div[@id="focus"]')
    header = [get_single_news.s(news_obj['link']) for news_obj in news_list]
    callback = task_notify.s()
    chord(header)(callback)


@custom_celery_task(name='get_single_news', retry_backoff=5, max_retries=3)
def get_single_news(url):
    news_dict = fetcher.get_news_content(url)  # title, content, author,
    data = {
        'title': news_dict['title'],
        'content': news_dict['content'],
        'author_name': news_dict['author'],
        'url': url
    }
    obj = News.objects.create(**data)  # noqa


@custom_celery_task()
def task_notify(result):
    notify_frontend()


def notify_frontend(*args, **kwargs):
    from channels.layers import get_channel_layer
    from asgiref.sync import async_to_sync

    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        'notifications',
        {
            'type': 'notify',
            'message': '任務已完成'
        }
    )


@task_postrun.connect
def task_postrun_handler(task_id, *args, **kwargs):
    """
    When celery task finish, send notification to Django channel_layer, so Django channel would receive
    the event and then send it to web client
    """
    if kwargs["sender"].name == 'news_crawler':
        notify_frontend()
