from django.urls import path

from .views import ArticleListView,ArticleRetrieveView


urlpatterns = [
path('',ArticleListView.as_view(),name='list'),
path('<pk>',ArticleRetrieveView.as_view(),name='detail')
]
