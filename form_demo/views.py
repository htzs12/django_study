from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .forms import RegisterForm
from .models import User


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
            print(form.errors.get_json_data())
            return HttpResponse('注册失败！')