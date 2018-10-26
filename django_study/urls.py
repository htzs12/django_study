"""django_study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orm/',include('db_orm.urls')),
    path('view/',include('method_view.urls')),
    path('form/',include('form_demo.urls')),
    path('cookie/',include('cookie_session.urls')),
    path('context/',include('content_process.urls')),
    path('icbc/',include('icbc.urls')),
    path('user/',include('users.urls')),
    path('mem/',include('mem_demo.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # url方式访问读取文件（列表用+）