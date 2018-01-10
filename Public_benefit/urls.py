"""Public_benefit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('welcome.urls')),  # 首页
    url(r'^pro_action/',include('pro_action.urls',namespace='pro_action')),  # 慈善项目和行动
    url(r'^user/',include('user.urls',namespace='user')),  # 用户模块
    url(r'^donate/',include('donate.urls',namespace='donate')),  # 捐赠模块
    url(r'^news/', include('news.urls', namespace='news')),  # 新闻资讯模块
    url(r'^information/', include('information.urls', namespace='information')),  # 信息公开模块

]
