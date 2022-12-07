from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from app1 import models
from django.template import RequestContext


# Create your views here.

def get(request, s):
    return request.POST.get(s)


def register(request):
    if request.method == "GET":
        # get请求直接返回页面
        return render(request, "inf_filling_student.html")
    if request.method == "POST":
        # 获取post请求数据
        name1 = get(request, "name")
        age1 = get(request, "age")
        gender0 = get(request, "gender")
        department0 = get("request", "department")
        grade0 = get(request, "grade")
        classroom0 = get(request, "classroom")
        party_is0 = get(request, "party_member_or_not")
        if (name1 == "" or name1 == null) or (age0 == "" or age0 == null) or (gender0 == "" or gender0 == null) or (department0 == "" or department0 == null) or (grade0 == "" or grade0 == null) or (classroom0 == "" or classroom0 == null) or (party_is0 == "" or party_is0 == null) or ():
            alert("Please fill all the required fields")
            return false
        # 判断post请求数据
        # if u == "":
        #     return render(request, "register.html", {"n1": "用户名不能为空!"})
        # elif p1 == "":
        #     return render(request, "register.html", {"n1": "密码不能为空!"})
        # elif p2 == "":
        #     return render(request, "register.html", {"n1": "确认密码不能为空!"})
        # elif p1 != p2:
        #     return render(request, "register.html", {"n1": "两次输入的密码不同!"})
        # else:
        #     # 查询数据库
        #     data_list = models.UserInf.objects.all()
        #     for obj in data_list:
        #         if u == obj.name:
        #             return render(request, "register.html", {"n1": "该用户名已被注册!"})
        #     """
        #     无查询结果，注册该用户，并返回提示登录信息
        #     """
        #     models.UserInf.objects.create(name=u, password=p1)
        #     return render(request, "register.html", {"n1": "注册成功!", "n2": "点击登录"})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')


def index(request):
    if request.method == "GET":
        return HttpResponse("请登录!")
    if request.method == "POST":
        u = get(request, 'name')


def manage(request):
    lessons_list = models.Lessons.objects.all()
    return render(request, "manage.html", {"lessons": lessons_list, })


def manage_add(request):
    if request.method == "POST":
        lesson_name0 = get(request, 'lesson_name')
        lesson_hour0 = get(request, 'lesson_hour')
        lesson_week0 = get(request, 'lesson_week')
        lesson_date0 = get(request, 'lesson_date')
        status0 = get(request, 'status')
        teacher0 = get(request, 'teacher')
        classroom0 = get(request, 'classroom')
        if lesson_name0 != '' and lesson_hour0 != '' and lesson_week0 != '' and lesson_date0 != '' and status0 != '' and classroom0 != '' and teacher0 != '':
            models.Lessons.objects.create(lesson_name=lesson_name0, lesson_hour=lesson_hour0, lesson_week=lesson_week0,
                                          lesson_date=lesson_date0, status=status0, teacher=teacher0,
                                          classroom=classroom0)
            return redirect("/manage/")
        return render(request, 'manage.html')