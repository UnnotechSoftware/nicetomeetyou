from django.urls import path

from .views import NewsList, NewsDetail


urlpatterns = [
    path("api/news/", NewsList.as_view()),
    path("api/news/<int:pk>/", NewsDetail.as_view()),
]
