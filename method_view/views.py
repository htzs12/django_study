from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse,JsonResponse
from django.views.generic import ListView
import json

from .models import Article


def index(request):
    print(request.get_host())
    print(request.GET)
    username = request.GET.get('username',default='haha')
    print(username)
    return HttpResponse('success')


def index1(request):
    person = {
        'username':'haoge',
        'age':20
    }
    # person_str = json.dumps(person)
    # response = HttpResponse(person_str,content_type='application/json')
    response = JsonResponse(person,safe=False) # safe=False 非字典类型需要设置
    return response


def index2(request):
    articles = []
    for x in range(0,102):
        article = Article(title='标题:%s'%x,content='内容:%s'%x)
        articles.append(article)
    Article.objects.bulk_create(articles)
    return HttpResponse('article added successfully.')


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = 'create_time'


