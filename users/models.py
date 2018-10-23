from django.db import models
from django.contrib.auth.models import User,Permission,ContentType
from django.contrib.auth import authenticate,login,logout
from django.dispatch import receiver
from django.db.models.signals import post_save

# class Person(User):
#     # 不能添加新的字段，Person是代理模型和User完全一样
#     class Meta:
#         proxy = True
#
#     @classmethod
#     def get_blacklist(cls):
#         return cls.objects.filter(is_active=False)


class UserExtension(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='extension')
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    telephone = models.CharField(max_length=11)
    school = models.CharField(max_length=100)


@receiver(post_save,sender=User)
def handler_extension(sender,instance,created,**kwargs):
    if created:
        UserExtension.objects.create(user=instance)
    else:
        instance.extension.save()

