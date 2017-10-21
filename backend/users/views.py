# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from users.models import Account
from posts.models import Post
from posts.serializers import PostOverviewSerializer


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        password_verify = request.POST['password2']
        try:
            user = User.objects.get(username=username)
            return render(request, 'users/signupd.html', {'errormsg': "Username already taken"})
        except User.DoesNotExist:
            if password == password_verify:
                user = User.objects.create_user(username=username, password=password)
                account = Account(user=user, certificate="None")
                account.save()
                login(request, user)
                return HttpResponse("signup success", status=200)
            else:
                return render(request, 'users/signupd.html', {'errormsg': "Passwords didn\'t match"})
    else:
        return render(request, 'users/signupd.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("login success", status=200)
        else:
            return render(request, 'users/logind.html', {'errormsg': "incorrect password"})
    else:
        return render(request, 'users/logind.html')


def logout_view(request):
    logout(request)
    return HttpResponse("logout success", status=200)


def user_posts_debug_view(request, user_id):
    if request.method == 'GET':
        try:
            cur_user = User.objects.get(username=user_id)
        except Exception:
            return JsonResponse({"status": "failure", "message": "user does not exist"}, status=404)
        user_posts = Post.objects.filter(author=cur_user).order_by('-votes_total')
        return render(request, 'posts/post-by-user-overview.html', {'user': cur_user, 'posts': user_posts})


def user_posts_view(request, user_id):
    if request.method == 'GET':
        try:
            cur_user = User.objects.get(username=user_id)
        except Exception:
            return JsonResponse({"status": "failure", "message": "user does not exist"}, status=404)
        user_posts = Post.objects.filter(author=cur_user).order_by('-votes_total')
        serializer = PostOverviewSerializer(user_posts, many=True)
        return JsonResponse(serializer.data, safe=False)