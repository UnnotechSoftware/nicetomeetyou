from django.urls import path
from backend.api import views
from backend.api.views import news_detail_page
from backend.api.views import news_timeline_page


urlpatterns = [
    path('news/', views.NewsTimeLine.as_view(), name='news-timeline'),
    path('news/<int:pid>', views.NewDetail.as_view(), name='news-detail'),
    path('news-page/', news_timeline_page, name='news-timeline-page'),
    path('news-page/<int:pid>', news_detail_page, name='news-detail-page'),
]
