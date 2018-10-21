from django.contrib.auth.models import User


# 自定义上下文管理器
def context_user(request):
    user_id = request.session.get('user_id')
    context = {}
    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except:
            pass
    return context
