from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from userprofile.forms import UserLoginForm, UserRegisterForm, ProfileForm
# 引入验证登陆的装饰器
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from userprofile.models import Profile

# Create your views here.

# 用户登陆
def user_login(request):
    """
    先判断是不是post请求
    然后把post请求数据给表单
        检测数据是否合法
        检验账号、密码是否正确匹配数据库中的某个用户
        如果均匹配则返回这个user对象
            将用户数据保存在session中,即实现了登陆动作
    """
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return redirect("article:article_list")
            else:
                return HttpResponse("账号或密码输入有误，请重新输入：")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == "GET":
        user_login_form = UserLoginForm()
        context = {
            'form': user_login_form
        }
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")    
        
# 用户退出
def user_logout(request):
    logout(request)
    return redirect("article:article_list")

# 用户注册
def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            # 设置密码
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            # 保存好数据后立即登录并返回博客列表页面
            login(request, new_user)
            return redirect("article:article_list")
        else:
            # 使用默认的表单的check函数不仅会检查密码是否相同，还会检查密码复杂程度，以及是否与其他信息相关等等
            return HttpResponse("注册表单输入有误。请重新输入~")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = { 'form': user_register_form }
        return render(request, 'userprofile/register.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")
    
# 用户删除
@login_required(login_url='/userprofile/login/')
def user_delete(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        # 验证登陆用户、待删除用户是否相同
        if request.user == user:
            # 退出登录，删除数据并返回博客列表
            logout(request)
            user.delete()
            return redirect("article:article_list")
        else:
            return HttpResponse("你没有删除操作的权限")
    else:
        return HttpResponse("仅接受post请求")

# 编辑用户信息    
@login_required(login_url='/userprofile/login/')
def profile_edit(request, id):
    """
    # user_id 是 OneToOneField 自动生成的字段
    """
    user = User.objects.get(id=id)
    # profile = Profile.objects.get(user_id=id)
    if Profile.objects.filter(user_id = id).exists():
        profile = Profile.objects.get(user_id=id)
    else:
        profile = Profile.objects.create(user=user)

    if request.method == 'POST':
        # 验证修改数据者，是否时用户本人
        if request.user != user:
            return HttpResponse("你没有权限修改此用户信息")
        
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_cd = profile_form.cleaned_data
            profile.phone = profile_cd['phone']
            profile.bio = profile_cd['bio']
            # 如果request.FILES存在文件，则保存
            if 'avatar' in request.FILES:
                profile.avatar = profile_cd["avatar"]
            profile.save()
            # 带参数的redirect()
            return redirect("userprofile:edit", id=id)
        else:
            return HttpResponse("注册表达那输入有误，请重新输入")
    elif request.method == 'GET':
        profile_form = ProfileForm()
        context = {
            'profile_form': profile_form,
            'profile': profile,
            'user': user
        } 
        return render(request, 'userprofile/edit.html', context)
    else:
        return HttpResponse("请使用get或post请求数据")
    