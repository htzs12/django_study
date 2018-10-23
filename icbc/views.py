from django.shortcuts import render
from django.views.generic import View


def index(request):
    return render(request,'icbc.html')


class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        pass


class RegisterView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        pass