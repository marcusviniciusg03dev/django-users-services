from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/users/login/')
def app_home(request: HttpRequest):
    return render(
        request,
        'app_home.html',
    )