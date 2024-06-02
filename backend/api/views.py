import logging

from django.core.cache import cache
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.api.models import News
from backend.api.serializers import NewsDetailSerializers
from backend.api.serializers import NewsTimelineSerializers
from backend.tasks.notifications import send_notification


logger = logging.getLogger(__name__)


class NewsTimeLine(APIView):

    @staticmethod
    def _setup_timeline_cache(news_data) -> None:
        logger.debug('Set up the news timeline to cache.')
        cache.set('news_timeline', news_data, timeout=60 * 15)

    @staticmethod
    def _get_news_data() -> dict:
        news = News.objects.all().order_by('-date_published')
        serializer = NewsTimelineSerializers(news, many=True)
        news_data = serializer.data
        return news_data

    def get(self, request) -> Response:
        logger.info('Received the request from getting news time line.')
        cached_news = cache.get('news_timeline')
        if cached_news:
            logger.info('Serving news timeline from cache.')
            return Response(cached_news, status=status.HTTP_200_OK)
        news_data = self._get_news_data()
        self._setup_timeline_cache(news_data=news_data)
        logger.info('Serving news timeline from database and caching it.')

        return Response(news_data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        data = request.data
        logger.info(f'Received the post nba news request: {data}')
        serializer = NewsDetailSerializers(data=data)
        if not serializer.is_valid():
            logger.warning(f'Fail to save the nba news to database.')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        news_data = self._get_news_data()
        self._setup_timeline_cache(news_data=news_data)
        send_notification()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class NewDetail(APIView):

    def get(self, request, pid: int) -> Response:
        logger.info(f'Received the request to get news detail for id: {pid}')
        if pid is None:
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        try:
            news = News.objects.get(pid=pid)
        except Exception as e:
            logger.error(str(e))
            news = None
        if not news:
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        serializer = NewsDetailSerializers(news)
        return Response(serializer.data, status=status.HTTP_200_OK)


def news_timeline_page(request):
    return render(request, 'news_timeline.html')


def news_detail_page(request, pid):
    return render(request, 'news_detail.html', {'pid': pid})
