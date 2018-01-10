from django.db import models
from user.models import User  # 导入User类，用来创建申请表的外键

"""
类型表：cate （在后台可以添加类型的分类）
主键：id
类型：name
是否删除：is_delete
"""
class Cate(models.Model):
    name = models.CharField(max_length=20)
    is_delete = models.BooleanField(default=False)


    class Meta:
        db_table = 'cate'


"""
项目表（项目和行动）：project

主键：id
项目名称：name
分类：pro_cate（外键）
项目内容：content
是否删除：is_delete	(默认为false不删除，true为删除)
项目和行动：pro_action （项目为true，行动为false）
"""
class Project(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    pro_cate = models.ForeignKey(Cate)
    pro_action = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)


    class Meta:
        db_table = 'project'



"""
申请表：apply

主键：id
申请人：apply_user（外键）
身份证照片：card_pic
申请资料：data_file
申请时间：createtime
慈善项目：apply_project（外键）
审核成功：is_success （审核成功将该项目添加到项目表中）
是否删除：is_delete
"""
class Apply(models.Model):
    apply_user = models.ForeignKey(User)  # 需要导入User类
    apply_project = models.ForeignKey(Project)
    card_pic = models.CharField(max_length=100)
    data_file = models.CharField(max_length=100)
    createtime = models.DateTimeField(auto_now_add=True)
    is_success = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)


    class Meta:
        db_table = 'apply'



"""
报名表：join

主键：id
申请人：join_user（外键）
慈善行动：join_action（外键）
申请时间：createtime
审核成功：is_success
是否删除：is_delete
"""
class Join(models.Model):
    join_user = models.ForeignKey(User)
    join_action = models.ForeignKey(Project)
    createtime = models.DateTimeField(auto_now_add=True)
    is_success = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)


    class Meta:
        db_table = 'join'

















