import logging

from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .models import News
# from .serializers import NewsSerializer


class NewsTimeLine(APIView):

    def get(self, request):
        logging.info('Received the request from getting news time line.')
        return Response(data={'hello': 'world!'}, status=status.HTTP_200_OK)

    def post(self, request):
        pass


class NewDetail(APIView):

    def get(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


