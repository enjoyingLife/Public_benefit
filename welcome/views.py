from django.shortcuts import render


# / 跳转首页
def index(request):
    return render(request, 'welcome/index.html')