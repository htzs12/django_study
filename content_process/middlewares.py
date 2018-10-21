from django.middleware.common import CommonMiddleware

# 中间件

# 函数方法


def user_middleware(get_response):
    # 执行一些初始化代码
    print('中间件初始化的代码')

    def middleware(request):
        print('request到达view之前执行的代码')
        # 在这个代码执行之前的代码，是request到view之前的代码
        response = get_response(request)
        print('response到达浏览器之前执行的代码')
        # response对象到达浏览器之前的执行代码
        return response
    return middleware


# 类方法

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response