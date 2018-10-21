from django import forms
from django.core import validators
from .models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}',
                                                                      message='请输入正确格式的手机号码！')])
    pwd1 = forms.IntegerField()
    pwd2 = forms.IntegerField()

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError(message='%s已经被注册~'%telephone)
        return telephone

    def clean(self):
        # 如果来到clearn方法，说明之前每一个字段都已经验证成功。
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError(message='两次密码输入不一致！')
        return cleaned_data




