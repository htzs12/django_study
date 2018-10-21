from django.db import models
from django.core import validators


class User(models.Model):
    username = models.CharField(max_length=100)
    telephone = models.CharField(max_length=11)


class File(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnial = models.FileField(upload_to='%Y/%m/%d/',validators=
    [validators.FileExtensionValidator(['txt'],message='必须为txt格式文件...')])

