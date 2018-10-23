from django.shortcuts import render
# from .models import Person
from django.http import HttpResponse
from django.contrib.auth.models import User


# def proxy_view(request):
    # user = User(username='hao',password='123456')
    # user.save()
    # blacklist = Person.get_blacklist()
    # for person in blacklist:
    #     print(person.username) # hao
    #
    # return HttpResponse('ok')


def my_authenticate(telephone,password):
    user = User.objects.filter(telephone=telephone).first()
    if user:
        is_correct = user.check_password(password)
        if is_correct:
            return user
        else:
            return None
    else:
        return None


def one_view(request):
    # user = User.objects.create_user(username='haogege',email='htzs@qq.com',password='111111')
    user = User.objects.create_user(username='haha6',email='htzs1@qq.com',password='222222')
    user.telephone = '18888888883'
    user.save()
    return HttpResponse('一对一模型')