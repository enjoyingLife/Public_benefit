from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse
from django.conf import settings

# /show_register 显示注册页面
def show_register(request):
    return render(request,'user/register.html')


# /login 登录页面
def login(request):
    return render(request, 'user/login.html')


# /login_check 登录验证
def login_check(request):
    """登录验证"""
    '''
    在数据库中查找用户信息，与之匹配
    '''
    # 取出数据库中所有元素
    all_users = User.objects.all()
    # 建立空列表保存 所有对象的名字和密码
    all_users_list = []
    for user in all_users:
        all_users_list.append((user.username, user.password))

    # return HttpResponse('登录成功')
    # 返回json数据 传给回调函数
    print(all_users_list)
    return JsonResponse({'res':all_users_list})


#-----------------注册模块----开始------------
#  /prov 显示省级数据
def get_prov(request):
    print('调用--省--函数成功')
    prov_datas = AreaInfo.objects.filter(aParent=None)
    prov_datas_list = []
    for data in prov_datas:
        prov_datas_list.append((data.id, data.atitle))
    return JsonResponse({"res": prov_datas_list})


# /city 显示市级数据
def get_city(request, pid):
    print('调用--市--函数成功')
    prov_datas = AreaInfo.objects.filter(aParent=pid)
    prov_datas_list = []
    for data in prov_datas:
        prov_datas_list.append((data.id, data.atitle))
    return JsonResponse({"res": prov_datas_list})


# /dis 显示县级数据
def get_dis(request, pid):
    print('调用--县--函数成功')
    prov_datas = AreaInfo.objects.filter(aParent=pid)
    prov_datas_list = []
    for data in prov_datas:
        prov_datas_list.append((data.id, data.atitle))
    return JsonResponse({"res": prov_datas_list})


# /add  将数据写入数据库
def add(request):
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    dis_id = request.POST.get('dpid')
    # print(username)
    # print(password)
    # print(dis_id)
    user = User()
    user.username = username
    user.password = password
    user.user_areas_id = dis_id
    user.name = '王杨'
    user.address = '123'
    user.birthday = '1995-6-9'
    user.email = '123'
    user.phone_num = '123123123'
    user.save()
    return HttpResponse('恭喜注册成功')
# ----------------注册模块----结束--------------

#-----------------上传文件模块--开始------------
# /upload_pic  显示上传文件页面
def upload_pic(request):
    return render(request, 'user/upload_pic.html')

# /upload_action 上传文件处理 写进数据库
def upload_action(request):
    # 获取一个上传的文件的对象
    pic =request.FILES.get('pic')
    # 建立一个保存文件的新目录
    save_path = '%s/user/%s'%(settings.MEDIA_ROOT, pic.name)
    # 开始读写文件
    with open(save_path, 'wb') as f:
        for content in pic.chunks():
            f.write(content)
    # 保存表中上传的路径
    path = 'user/%s' % pic.name
    # 写入数据库
    Goods.objects.create(pic = path)
    return HttpResponse('<h1>上传成功</h1>')


#-----------------上传文件模块--结束------------





