from django.shortcuts import render


# /show_project 展示慈善项目页面
def show_project(request):
    return render(request,'pro_action/project.html')


# /show_action 显示慈善行动页面
def show_action(request):
    return render(request,'pro_action/action.html')


# /show_apply 显示申请项目页面
def show_apply(request):
    return render(request,'pro_action/apply.html')


# /deal_apply 处理申请项目内容    关于下一步分两次提交表单的问题
def deal_apply(request):
    return render(request,'pro_action/check_data.html')

# /check_apply 审核申请项目资料






















