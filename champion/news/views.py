from django.shortcuts import render, get_object_or_404
from .models import News

def news(request):
    news = News.objects.all()
    return render(request, 'news/news.html', context={'news': news})

def news_detail(request, news_slug):
    news = get_object_or_404(News, slug=news_slug)
    return render(request, 'news/news_detail.html', context={'news': news})
