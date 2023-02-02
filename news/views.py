from typing import Type

from django.shortcuts import render, redirect
from .models import News
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import ArticlesFrom


# функция с главной страницей приложения news
def main_news(request):
    return render(request, 'news/main_news.html')


# функция показа статей
def article_news(request):
    news = News.objects.all()
    return render(request, 'news/article_news.html', {'news': news})

#функция для детального просмотра статьи
class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail_view.html'
    context_object_name = 'article'

#редактирование статьи
class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/article_forms.html'

    form_class = ArticlesFrom

#Удаление статьи
class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/news-delete.html'
    success_url = '/news/articles'

#функция добавления записи в бд
def news_forms(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news')
        else:
            error = 'Форма была неверной'

    forms = ArticlesFrom()

    data = {
        'form': forms,
        'error': error
    }
    return render(request, 'news/article_forms.html', data)