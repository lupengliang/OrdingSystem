from django.db import models

from datetime import datetime

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)  # 员工账号
    nickname = models.CharField(max_length=50)  # 昵称
    password_hash = models.CharField(max_length=100)  # 密码
    password_salt = models.CharField(max_length=50)  # 密码干扰值
    status = models.IntegerField(default=1)  # 状态：1正常/2禁用/6管理员/9删除
    create_at = models.DateTimeField(default=datetime.now)  # 创建时间
    update_at = models.DateTimeField(default=datetime.now)  # 修改时间

    def toDict(self):
        return {"id": self.id, "username": self.username, "nickname": self.nickname, "password_hash": self.password_hash}

    class Meta:
        db_table = "user"  # 更改表名


# 店铺信息模型
class Shop(models.Model):
    name = models.CharField(max_length=255)  # 店铺名称
    cover_pic = models.CharField(max_length=255)  # 封面图片
    banner_pic = models.CharField(max_length=255)  # 图标Logo
    address = models.CharField(max_length=255)  # 店铺地址
    phone = models.CharField(max_length=255)  # 联系电话
    status = models.IntegerField(default=1)  # 状态1正常/2暂停/9删除
    create_at = models.DateTimeField(default=datetime.now)  # 创建时间
    update_at = models.DateTimeField(default=datetime.now)  # 修改时间

    def toDict(self):
        shopname = self.name.split("-")
        return {'id': self.id, 'name': shopname[0], 'shop': shopname[1], 'cover_pic': self.cover_pic, 'banner_pic': self.banner_pic}

    class Meta:
        db_table = "shop"  # 更改表名
