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


# 菜品分类信息模型
class Category(models.Model):
    shop_id = models.IntegerField()  # 店铺id
    name = models.CharField(max_length=50)  # 分类名称
    status = models.IntegerField(default=1)  # 状态1正常、9删除
    create_at = models.DateTimeField(default=datetime.now)  # 创建时间
    update_at = models.DateTimeField(default=datetime.now)  # 修改时间

    class Meta:
        db_table = "category"  # 更改表名


# 菜品信息类型
class Product(models.Model):
    shop_id = models.IntegerField()  # 店铺id
    category_id = models.IntegerField()  # 菜品分类id
    cover_pic = models.CharField(max_length=50)  # 菜品图片
    name = models.CharField(max_length=50)  # 菜品名称
    price = models.FloatField()  # 菜品单价
    status = models.IntegerField(default=1)  # 状态1正常/2停售/9删除
    create_at = models.DateTimeField(default=datetime.now)  # 创建时间
    update_at = models.DateTimeField(default=datetime.now)  # 修改时间

    def toDict(self):
        return {'id': self.id, 'shop_id': self.shop_id, 'category_id': self.category_id}

    class Meta:
        db_table = "product"  # 更改表名


# 会员信息模型
class Member(models.Model):
    nickname = models.CharField(max_length=50)  # 昵称
    avatar = models.CharField(max_length=255)  # 头像
    mobile = models.CharField(max_length=50)  # 电话
    status = models.IntegerField(default=1)  # 状态1正常/2禁用/9删除
    create_at = models.DateTimeField(default=datetime.now)  # 创建时间
    update_at = models.DateTimeField(default=datetime.now)  # 修改时间

    def toDict(self):
        return {'id': self.id, 'nickname': self.nickname, 'avatar': self.avatar, 'mobile': self.mobile, 'status': self.status}

    class Meta:
        db_table = "member"  # 更改表名
