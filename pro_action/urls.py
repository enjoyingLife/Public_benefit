from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^show_project$',views.show_project,name='show_project'),  # 展示慈善项目页面
    url(r'^show_action$',views.show_action,name='show_action'),  # 展示慈善行动页面
    url(r'^show_apply$',views.show_apply,name='show_apply'),  # 展示申请项目页面
    url(r'^deal_apply$',views.deal_apply,name="deal_apply"),  # 处理申请项目内容
]
