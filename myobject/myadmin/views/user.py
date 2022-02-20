# 员工信息管理的视图文件
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from myadmin.models import User

# Create your views here.
def index(request, pIndex=1):
    """浏览信息"""
    umod = User.objects
    ulist = umod.filter(status_lt=9)

    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(ulist, 5)  # 每页5条数据分页
    maxpages = page.num_pages  # 获取最大页数
    # 判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 获取当前页数据
    plist = page.page_range  # 获取页码列表信息
    context = {"userlist": ulist, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages}
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
