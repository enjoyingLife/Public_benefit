from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

# 定义数据库字段

class AreaInfo(models.Model):
    """地区模型类"""
    atitle = models.CharField(verbose_name='名称', max_length=20)  # 地区名称
    aParent = models.ForeignKey('self', null=True, blank=True)  # 自关联属性

    def title(self):
        """返回当前地区的标题"""
        return self.atitle

    title.admin_order_field = 'atitle'
    title.short_description = '地区名称'

    def parent(self):
        """返回当前地区的父级地址的标题"""
        if self.aParent is None:
            return '无'
        return self.aParent.atitle

    parent.short_description = '父级地区名称'

    def __str__(self):
        """返回地区的标题"""
        return self.atitle

    class Meta:
        db_table = 'areas'

"""
用户user表字段：

主键：id
账号：username[可以是邮箱和手机号，注册详细信息的时候自动弹出对应的邮箱和手机号]
密码：password
姓名：name
性别：gender
邮箱：email
出生日期：birthday
联系方式：phone_num
家庭住址：address
创建时间：createtime
更改时间：updatetime
"""
class User(models.Model):
    """用户设计"""
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)  # 默认True是男
    email = models.CharField(max_length=40)
    birthday = models.DateField()
    phone_num = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    createtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
    user_areas = models.ForeignKey(AreaInfo)  # 外键命名规范：本表名_关联的表名
    class Meta:
        db_table = 'user'


    def __str__(self):
        """对象返回值"""
        return self.username

# 这个模型类移动到pro_action的模块中了
class Goods(models.Model):
    """图片类"""
    pic = models.ImageField(upload_to='user')

    class Meta:
        db_table = 'goods'

"""
用户和项目的关联表：user_project

用户id：user_id
项目id：project_id
慈善等级：grade	(根据捐款的数量评定)
捐（收）钱：money
捐（收）物：goods
关注：is_attention(默认为null，关注为true，取消为false)	用户点击关注
参加：is_join（默认为null，参加为true，删除为false）后台审核通过
帮助：is_help（默认为null，帮助为true，删除为false）转账之后或将物资运到后台之后
申请：is_apply（默认为null，申请为true，删除为false，删除的同时将项目表中的is_delete改为true）后台审核通过
创建的时间：createtime
更改的时间：updatetime
"""
class UserProject(models.Model):
    user_id = models.IntegerField()
    project_id = models.IntegerField()
    grade = models.IntegerField()
    money = models.DecimalField(max_digits=12,decimal_places=2)
    goods = models.CharField(max_length=100)
    is_attention = models.NullBooleanField(default=None)
    is_join = models.NullBooleanField(default=None)
    is_help = models.NullBooleanField(default=None)
    is_apply = models.NullBooleanField(default=None)
    createtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'user_project'




























