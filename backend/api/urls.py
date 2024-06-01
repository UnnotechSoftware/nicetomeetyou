from django.urls import path
from backend.api import views

urlpatterns = [
    path('news/', views.NewsTimeLine.as_view(), name='news-timeline'),
    path('news/<int:pid>', views.NewDetail.as_view(), name='news-detail'),
]
