from django.urls import path, include
from news.views import *


urlpatterns = [
    path('', main_news),
    path('articles/', article_news),
    path('articles/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('articles/forms', news_forms),
    path('articles/<int:pk>/update', NewsUpdateView.as_view(), name='news-update'),
    path('articles/<int:pk>/delete', NewsDeleteView.as_view(), name='news-delete')
]
