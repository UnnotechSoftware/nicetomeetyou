from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import News
from .pagination import CustomPagination
from .renderer import CustomJSONRenderer
from .serializers import NewsSerializer


class NewsList(APIView, CustomPagination):
    # renderer_classes = [CustomJSONRenderer]

    def get(self, request, format=None):  # noqa
        # CustomPagination().paginate_queryset(News.objects.all(), request)
        movies = CustomPagination().paginate_queryset(News.objects.all(), request)  # noqa
        print('movies', movies, flush=True)
        serializer = NewsSerializer(movies, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):  # noqa
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsDetail(APIView):
    # renderer_classes = [CustomJSONRenderer]

    def get_object(self, pk):  # noqa
        try:
            return News.objects.get(pk=pk)  # noqa
        except News.DoesNotExist:  # noqa
            raise Http404

    def get(self, request, pk, format=None):  # noqa
        movie = self.get_object(pk)
        serializer = NewsSerializer(movie)
        return Response(serializer.data)
