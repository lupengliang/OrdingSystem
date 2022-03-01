from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'myadmin/index/index.html')

# 管理员登录表单
def login(request):
    return render(request, 'myadmin/index/login.html')

# 执行管理员登录
def dologin(request):
    pass

# 管理员退出
def logout(request):
    pass
