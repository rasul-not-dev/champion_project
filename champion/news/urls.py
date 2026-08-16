from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('<slug:news_slug>/', views.news_detail, name='news_detail')
]
