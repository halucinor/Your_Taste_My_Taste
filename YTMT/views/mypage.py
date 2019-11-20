from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from YTMT.models import *
from django.contrib import auth
import datetime
from . import session as SS
from . import utils 

# 마이페이지_수정
def mypagemain(request):
    return render(request, 'mypage/mypagemain.html')

# 마이페이지_개인정보 수정
def selectinfo(request):
    return render(request, 'mypage/selectinfo.html')

def infomodify(request):
    return render(request, 'mypage/infomodify.html')

def infomodifysave(request):
    login_user = SS.find_user(request)

    if request.method == "POST":
        if request.POST["pwd"] == request.session.get('password'):
            if request.POST["newpwd"] == request.POST["pwdchk"]:
                login_user.set_password(request.POST["newpwd"])
                request.session['password'] = request.POST["newpwd"]
                if request.POST["email2"] != "etc":
                    login_user.email = request.POST["email"] + "@" + request.POST["email2"]
                else:
                    login_user.email = request.POST["email"]
                login_user.save()
                return render(request, 'mypage/selectinfo.html')
            return render(request,'mypage/infomodify.html')
        return render(request,'mypage/infomodify.html')
    return render(request,'mypage/infomodify.html')

def religionmodify(request):
    return render(request, 'mypage/religionmodify.html')

def religionmodifysave(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)

    reli_name = request.POST.get("religion")
    userProfile.reli_id = utils.get_reli_id(reli_name)

    userProfile.save()
    return render(request, 'mypage/selectinfo.html')

def vegetarianmodify(request):
    return render(request, 'mypage/vegetarianmodify.html')

def vegetarianmodifysave(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)

    vege_name = request.POST.get("vegetarian")
    userProfile.vege_id = utils.get_vege_id(vege_name)

    userProfile.save()
    return render(request, 'mypage/selectinfo.html')

def allergymodify(request):
    return render(request, 'mypage/allergymodify.html')

def allergymodifysave(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)

    # 일대다
    return render(request, 'mypage/selectinfo.html')

def hatemodify(request):
    return render(request, 'mypage/hatemodify.html')

def hatemodifysave(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)

    return render(request, 'mypage/selectinfo.html')

# 마이페이지_기타
def history(request):
    return render(request, 'mypage/history.html')

def friendlist(request):
    return render(request, 'mypage/friendlist.html')