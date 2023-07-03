from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def signin(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/app')
        else:
            return render(
                request,
                'login.html',
                {
                    'error_message': 'Check your credentials.'
                }
            )
    else:
        return HttpResponse('Resource not found.')

def register(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username == None or email == None or password == None:
            return render(
                request,
                'register.html',
                {
                    'error_message': 'Some data is missing.'
                })
        
        if len(username) == 0 or len(email) == 0 or len(password) == 0:
            return render(
                request,
                'register.html', {
                    'error_message': 'No fields can be empty.'
                })

        finded_user = User.objects.filter(username=username).first()

        if finded_user != None:
            return render(
                request,
                'register.html', {
                    'error_message': 'Check your credentials.' 
                })
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse('User successfully created.')
    else:
        return HttpResponse('Resource not found.')