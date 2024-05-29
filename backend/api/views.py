import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.api.models import News
from backend.api.serializers import NewsSerializers


logger = logging.getLogger(__name__)


class NewsTimeLine(APIView):

    def get(self, request):
        logger.info('Received the request from getting news time line.')
        news = News.objects.all().order_by('-date_published')
        serializer = NewsSerializers(news, many=True)
        news = serializer.data
        return Response(news, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        logger.info(f'Received the post nba news request: {data}')
        serializer = NewsSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning(f'Fail to save the nba news to database.')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewDetail(APIView):

    def get(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


