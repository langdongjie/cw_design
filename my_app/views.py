from django.shortcuts import render

# coding:utf-8
from django.http import HttpResponse
from .self_class.recognition import Recognition
from .self_class.login import LoginManager


def login(request):
    if request.method == 'GET':
        return render(request, "login.html", {"message": ""})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        login_manager = LoginManager()
        if login_manager.login(username, password):
            print(username)
            LoginManager.username = username
            return render(request, "index.html", {"username": LoginManager.username})
    return render(request, "login.html", {"message": "密码输入错误或用户名不存在"})


def register(request):
    if request.method == 'GET':
        return render(request, "register.html", {"message": ""})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        LoginManager().register(username, email, password)
    return render(request, "register.html", {"message": "注册成功"})


def textMining(request):
    url = ""
    wordcloud_path = ""
    summary_str = ""
    if request.method == 'POST':
        url = request.POST.get('url')
        re = Recognition(url)
        wordcloud_path = re.get_wordcloud()
        summary_str = re.get_summary(3)
    return render(request, "textMining.html", {"url": url,
                                               "wordcloud": wordcloud_path,
                                               "summary": summary_str,
                                               "username": LoginManager.username})


def dataAnalysis(request):
    return render(request, "dataAnalysis.html", {"username": LoginManager.username})


def index(request):
    return render(request, "index.html", {"username": LoginManager.username})


def projectDesc(request):
    return render(request, "projectDesc.html", {"username": LoginManager.username})


def selfCenter(request):
    return render(request, "selfCenter.html", {"username": LoginManager.username})


def tech(request):
    return render(request, "tech.html", {"username": LoginManager.username})

#
# def factors_to_identify(request):
#     url = "我是傻逼"
#     wordcloud_path = ""
#     summary_str = ""
#     if request.method == 'POST':
#         url = request.POST.get('url')
#         re = Recognition(url)
#         wordcloud_path = re.get_wordcloud()
#         summary_str = re.get_summary(3)
#     return render(request, "main.html", {"wordcloud": wordcloud_path, "summary": summary_str})



