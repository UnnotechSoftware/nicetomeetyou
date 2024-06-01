import logging

from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.api.models import News
from backend.api.serializers import NewsDetailSerializers
from backend.api.serializers import NewsTimelineSerializers


logger = logging.getLogger(__name__)


class NewsTimeLine(APIView):

    def get(self, request):
        logger.info('Received the request from getting news time line.')
        cached_news = cache.get('news_timeline')
        if cached_news:
            logger.info('Serving news timeline from cache.')
            return Response(cached_news, status=status.HTTP_200_OK)

        news = News.objects.all().order_by('-date_published')
        serializer = NewsTimelineSerializers(news, many=True)
        news_data = serializer.data
        cache.set('news_timeline', news_data, timeout=60 * 15)
        logger.info('Serving news timeline from database and caching it.')

        return Response(news_data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        logger.info(f'Received the post nba news request: {data}')
        serializer = NewsTimelineSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning(f'Fail to save the nba news to database.')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewDetail(APIView):

    def get(self, request, pid):
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
