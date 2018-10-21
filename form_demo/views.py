from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .forms import RegisterForm,FileForm
from .models import User,File


class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            telephone = form.cleaned_data.get('telephone')
            pwd1 = form.cleaned_data.get('pwd1')
            pwd2 = form.cleaned_data.get('pwd2')
            print(pwd1,pwd2)
            User.objects.create(username=username,telephone=telephone)
            return HttpResponse('注册成功')
        else:
            print(form.get_errors())
            return HttpResponse('注册失败！')


# 文件上传功能
class FileView(View):
    def get(self,request):
        return render(request,'files.html')

    def post(self,request):
        # myfile = request.FILES.get('myfile')
        # with open('somefile.txt','wb') as fp:
        #     for chunk in myfile.chunks():
        #         fp.write(chunk)
        # return HttpResponse('success')
        # ----------------------------------------------------
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # file = request.FILES.get('myfile')
        # File.objects.create(title=title,content=content,thumbnial=file)
        # return HttpResponse('success')

        # ----------------------------------------------------
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            print(form.errors.get_json_data())
            return HttpResponse('fail')
