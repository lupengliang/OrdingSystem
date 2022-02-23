# 员工信息管理的视图文件
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q

from datetime import datetime

from myadmin.models import User

# Create your views here.
def index(request, pIndex=1):
    """浏览信息"""
    umod = User.objects
    ulist = umod.filter(status__lt=9)
    mywhere = []

    # 获取并判断搜索条件
    kw = request.GET.get('keyword', None)
    if kw:  # Q表示或者的条件
        ulist = ulist.filter(Q(username__contains=kw) | Q(nickname__contains=kw))
        mywhere.append('keyword='+kw)
    # 获取、判断并封装状态status搜索条件
    status = request.GET.get('status', '')
    if status != '':
        ulist = ulist.filter(status=status)
        mywhere.append("status="+status)

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
    context = {"userlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "myadmin/user/index.html", context)


def add(request):
    """加载信息添加表单"""
    try:
        ob = User()
        ob.username = request.POST['username']
        ob.nickname = request.POST['nickname']
        ob.status = 1
        ob.username = request.POST['username']
        ob.create_at = request.POST['create_at']
        ob.update_at = request.POST['update_at']
        ob.save()
        context = {'info': "添加成功！"}
    except Exception as err:
        print(err)
        print(err)
        context = {'info': "添加失败！"}
    # return render(request, "myadmin/info.html", context)
    return HttpResponse("ok")

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
