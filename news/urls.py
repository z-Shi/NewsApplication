from django.urls import path
from news.views import NewsView, ShowMoreView


app_name = 'news'

urlpatterns = [
    path('', NewsView.as_view(), name='index'),
    path('show_more/', ShowMoreView.as_view(), name='show_more'),
]
