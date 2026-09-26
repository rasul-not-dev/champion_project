from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News

def news(request):
    news = News.objects.all()

    paginator = Paginator(news, 6)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'news/news.html', context={'news': page_obj})

def news_detail(request, news_slug):
    news = get_object_or_404(News, slug=news_slug)
    return render(request, 'news/news_detail.html', context={'news': news})
