from django import forms
from django.core import validators
from .models import User,File


class BaseForm(forms.Form):
    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key,message_dicts in errors.items():
            messages = []
            for message_dict in message_dicts:
                message = message_dict['message']
                messages.append(message)
            new_errors[key] = messages
        return new_errors


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

    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key,message_dicts in errors.items():
            messages = []
            for message_dict in message_dicts:
                message = message_dict['message']
                messages.append(message)
            new_errors[key] = messages
        return new_errors

    def clean(self):
        # 如果来到clearn方法，说明之前每一个字段都已经验证成功。
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError(message='两次密码输入不一致！')
        return cleaned_data


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
        error_messages = {
            'thumbnial' : {
                'invalid_extension':'请上传正确格式的文件...'
        }}