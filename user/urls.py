from django.conf.urls import url
from . import views

urlpatterns = [
    #----------------用户信息和验证---------------------
    url(r'^show_register$',views.show_register,name='show_register'),  # 显示注册页面
    url(r'^login$', views.login, name='login'),# 用户登录界面
    url(r'^login_check', views.login_check), # 用户登录验证

    #-------------------写入数据库----------------------
    url(r'^prov$', views.get_prov),# 显示省级数据
    url(r'^city/(?P<pid>\d+)$', views.get_city),# 显示市级数据
    url(r'^dis/(?P<pid>\d+)$', views.get_dis),  # 显示县级数据
    url(r'^add$', views.add),# 将注册信息写入数据库

    # -------------------上传文件-----------------------
    url(r'^upload_pic$', views.upload_pic), # 显示上传页面
    url(r'^upload_action$', views.upload_action), # 上传文件处理


]
