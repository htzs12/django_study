from django.shortcuts import render
from django.http import HttpResponse

from .models import Article,Book,BookOrder,Publisher,Author
from django.db.models import Avg,Count,Max,Min,Sum,F,Q
from django.db import connection


# def exact(request):

    # exact 精确查找
    # article = Article.objects.filter(title__exact='django学习')
    # print(article)
    # print(article.query)
    # SELECT "db_orm_article"."id", "db_orm_article"."title"
    # FROM "db_orm_article" WHERE "db_orm_article"."title" = django学习

    # iexact 精确查找
    # article1 = Article.objects.filter(title__iexact='django学习')
    # print(article1.query)
    # SELECT "db_orm_article"."id", "db_orm_article"."title"
    # FROM "db_orm_article" WHERE "db_orm_article"."title" LIKE django学习

    # exact 和 iexact  区别 : = 和 like

    # exact 等价于 = ,直接使用 (title='xxx')

    # queryset.query 可以查询数据库查询语句，get方法不可以~

#     return HttpResponse('hello world...')
#
#
# def contains(request):
#     reslut = Article.objects.filter(title__contains='django')
    # contains 查询数据是否在其中 分大小写

    # SELECT "db_orm_article"."id", "db_orm_article"."title"
    # FROM "db_orm_article" WHERE "db_orm_article"."title" LIKE %django%

    # print(reslut.query)
    #
    # reslut1 = Article.objects.filter(title__icontains='django')

    # icontains 查询数据是否在其中 不分大小写

    # print(reslut1.query)

    # return HttpResponse('hello world...')

# 其他方法查文档即可。。。

# ========================================================================



#  聚合函数的应用


# 1. 获取所有图书的定价的平均价


# def model(request):
#     # result = Book.objects.aggregate(Avg('price')) # {'price__avg': 97.25}
#     result = Book.objects.aggregate(avg=Avg('price')) # {'avg': 97.25}
#     print(result)
#     print(connection.queries)
#     return HttpResponse('sucess')
#
#
# # 2. 获取每一本图书销售的平均价格
#
# def model1(request):
#     books = Book.objects.annotate(avg=Avg('bookorder__price'))
#     for book in books:
#         print('%s/%s'%(book.name,book.avg))
#     print(connection.queries)
#     return HttpResponse('sucess')


# book表中总共多少本书

# def model2(request):
#     # result = Book.objects.aggregate(book_nums=Count('id')) # 4
#     result = Author.objects.aggregate(email_nums=Count('email',distinct=True)) # 过滤相同的 /3
#     # print(result)
#     print(result)
#     print(connection.queries)
#     return HttpResponse('sucess')
#
#
# # 统计每本书的销量
#
# def model3(request):
#     books = Book.objects.annotate(book_nums=Count('bookorder__id'))
#     for book in books:
#         print('%s/%s'%(book.name,book.book_nums))
#
#     print(connection.queries)
#     return HttpResponse('sucess')
#
#
# # 获取每一本书的最大价格和最小价格
#
# def model4(request):
#     books = Book.objects.annotate(max=Max('bookorder__price'),min=Min('bookorder__price'))
#     for book in books:
#         print('%s/%s/%s'%(book.name,book.max,book.min))
#
#     print(connection.queries)
#     return HttpResponse('sucess')
#
#
# # 求所有图书销售总额
#
# def model5(request):
#     result = Book.objects.aggregate(total=Sum('price'))
#
#     # {'total': 389.0}
#
#     print(result)
#     print(connection.queries)
#     return HttpResponse('sucess')
#
#
# # 每一本书的销售总额
#
#
# def model6(request):
#     books = Book.objects.annotate(total=Sum('bookorder__price'))
#
#     # 三国演义 / 268.0
#     # 水浒传 / 187.0
#     # 西游记 / None
#     # 红楼梦 / None
#
#     for book in books:
#         print('%s/%s'%(book.name,book.total))
#
#     print(connection.queries)
#     return HttpResponse('sucess')
#
#
# # 求2018年度销售额
#
# def model7(request):
#     result = BookOrder.objects.filter(create_time__year=2018).aggregate(total=Sum('price'))
#
#     # {'total': 455.0} / {'total': 360.0}
#
#     print(result)
#     print(connection.queries)
#     return HttpResponse('sucess')
#
#
# # 求每一本图书2018销售额
#
#
# def model8(request):
#     books = Book.objects.filter(bookorder__create_time__year=2018).annotate(total=Sum('bookorder__price'))
#     for book in books:
#         print('%s/%s'%(book.name,book.total))
#
#     # 三国演义 / 173.0
#     # 水浒传 / 187.0
#
#     print(connection.queries)
#     return HttpResponse('sucess')
#
#
# # ========================================================================
#
# # F / Q 表达式
#
# # 给每一本图书增加10元
#
# def model9(request):
#     Book.objects.update(price=F('price')+10)  # 动态获取字段的值，不会执行数据库操作.
#
#     print(connection.queries[-1])
#
#     return HttpResponse('sucess')

# {'sql': 'UPDATE "book" SET "price" = ("book"."price" + 10)', 'time': '0.002'}


# Q表达式可以实现并集等各种查询


# ========================================================================


# filter方法
# 找出id 不等于3的

# def model10(request):
#     # books = Book.objects.filter(~Q(id=3))
#     books = Book.objects.exclude(id=3)
#     for book in books:
#         print(book)
#     return HttpResponse('success')

# Book object (1)
# Book object (2)
# Book object (4)


# annotate方法,为每个对象都添加一个使用查询表达式的新字段

# def model11(request):
#     books = Book.objects.annotate(author_name=F('author__name'))
#     for book in books:
#         # print(book.name)
#         # print(book.author.name)
#         # print(book.author_name)
#     return HttpResponse('success')

# 三国演义
# 水浒传
# 西游记
# 红楼梦

# 罗贯中
# 施耐庵
# 吴承恩
# 曹雪芹



