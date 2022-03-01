# 后台管理子路由文件
from django.contrib import admin
from django.urls import path

from myadmin.views import index
from myadmin.views import user

urlpatterns = [
    path('', index.index, name="myadmin_index"),  # 后台首页

    # 后台管理员登录、退出路由
    path('login', index.login, name="myadmin_login"),  # 加载登录表单
    path('dologin', index.dologin, name="myadmin_dologin"),  # 执行登录
    path('logout', index.logout, name="myadmin_logout"),  # 退出

    # 员工信息管理路由
    path('user/<int:pIndex>', user.index, name="myadmin_user_index"),  # 浏览
    path('user/add', user.add, name="myadmin_user_add"),  # 添加表单
    path('user/insert', user.insert, name="myadmin_user_insert"),  # 执行添加
    path('user/del/<int:uid>', user.delete, name="myadmin_user_delete"),  # 执行删除
    path('user/edit/<int:uid>', user.edit, name="myadmin_user_edit"),  # 加载编辑表单
    path('user/update/<int:uid>', user.update, name="myadmin_user_update"),  # 执行编辑
]
