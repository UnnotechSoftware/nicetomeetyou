from django.urls import path

from .views import NewsList, NewsDetail


urlpatterns = [
    path("news/", NewsList.as_view()),
    path("news/<int:pk>/", NewsDetail.as_view()),
]
