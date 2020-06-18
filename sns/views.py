from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import SearchForm
from .forms import ArticleForm
from .models import Comments



def index(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        articles = Article.ojects.filler(content__contains=keyword)
    else:
        searchForm = SearchForm()
        articles = Article.objects.all()

    context = {
        'message': 'Welcome my BBS',
        'articles': articles,
        'searchForm': searchForm,
    }
    return render(request, 'sns/index.html', context)


def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    # comment = get_object_or_404(Comments)
    # user_name = get_object_or_404(Comments)
    context = {
        'message': 'Show Article' + str(id),
        'article': article,
        # 'comment': comment,
        # 'user_name': user_name,

    }
    return render(request, 'sns/detail.html', context)


def new(request):
    articleForm = ArticleForm()

    context = {
        'message': 'New Article',
        'articleForm': articleForm,
    }
    return render(request, 'sns/new.html', context)


def create(request):
    if request.method == 'POST':
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid():
            article = articleForm.save()

    context = {
        'message': 'Create article' + str(article.id),
        'article': article,
    }
    return render(request, 'sns/detail.html', context)


def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    articleForm = ArticleForm(instance=article)
    context = {
        'message': 'Edit Article' + str(id),
        'article': article,
        'articleForm': articleForm,
    }
    return render(request, 'sns/edit.html', context)


def update(request, id):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=id)
        articleForm = ArticleForm(request.POST, instance=article)
        if articleForm.is_valid():
            articleForm.save()

    context = {
        'message': 'Update article ' + str(id),
        'article': article,
    }
    return render(request, 'sns/detail.html', context)


def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()
    articles = Article.objects.all()

    context = {
        'message': 'Delete Article' + str(id),
        'articles': articles,
    }
    return render(request, 'sns/index.html', context)
