from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError

def reg(request):
    context = {}
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        context["login"] = login
        context["password"] = password
        context["confirm_password"] = confirm_password

        if login and password and confirm_password:
            if len(password) >= 8:
                if password == confirm_password:
                    try:
                        User.objects.create_user(
                            username=login,
                            password=password
                        )
                        return redirect('auth')
                    except IntegrityError:
                        context['error'] = ''
                else:
                    context["error"] = ''
            else:
                context["error"] = ''
        else:
            context["error"] = ''
        

                    
    return render(request, 'auth_reg/reg.html')

def auth(request):
    context = {}
    if request.user.is_authenticated:
        context['error'] = 'You already authorisated'
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                return redirect('main')
            else:
                context['error'] = 'login or password false'
        else:
            context['error'] = 'write all input'
    return render(request, 'auth_reg/auth.html')


def user_logout(request):
    logout(request)
    return redirect('auth')