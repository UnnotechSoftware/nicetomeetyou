from django.http import Http404
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .models import News
from .pagination import CustomPagination
from .serializers import NewsSerializer


class NewsList(APIView, CustomPagination):
    permission_classes = [AllowAny]

    def get(self, request, format=None):  # noqa
        news = News.objects.all()  # noqa
        result = self.paginate_queryset(news, request, view=self)  # noqa
        serializer = NewsSerializer(result, many=True)

        return self.get_paginated_response(serializer.data)


class NewsDetail(APIView, CustomPagination):
    permission_classes = [AllowAny]

    def get_object(self, pk):  # noqa
        try:
            return News.objects.get(pk=pk)  # noqa
        except News.DoesNotExist:  # noqa
            raise Http404

    def get(self, request, pk, format=None):  # noqa
        news = self.get_object(pk)
        result = self.paginate_queryset(news, request, view=self)  # noqa
        serializer = NewsSerializer(result, many=True)

        return self.get_paginated_response(serializer.data)
