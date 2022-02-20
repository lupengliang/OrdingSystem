# 员工信息管理的视图文件
from django.shortcuts import render
from django.http import HttpResponse

from myadmin.models import User

# Create your views here.
def index(request):
    """浏览信息"""
    umod = User.objects
    ulist = umod.all()
    context = {"userlist": ulist}
    return render(request, "myadmin/user/index.html", context)

def add(request):
    """加载信息添加表单"""
    pass

def insert(request):
    """执行信息添加"""
    pass

def delete(request, uid=0):
    """执行信息删除"""
    pass

def edit(request, uid=0):
    """加载信息编辑表单"""
    pass

def update(request, uid):
    """执行信息编辑"""
    pass
