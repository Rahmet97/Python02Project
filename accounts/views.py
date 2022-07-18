from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(username=username)
        print(user)
        if check_password(password, user.password):
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Username or password is invalid!")
            return redirect('login')
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        name = request.POST["name"]
        surname = request.POST["surname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password_check = request.POST["password_check"]

        if password == password_check:
            if User.objects.filter(username=username).exists():
                messages.error(request, "This username is already exists!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "This email is already exists!")
                return redirect('register')
            else:
                user = User.objects.create(
                    first_name=name,
                    last_name=surname,
                    username=username,
                    email=email,
                    password=make_password(password)
                )
                user.save()
                return redirect('login')
        else:
            messages.error(request, "Passwords are not similar")
            return redirect('register')
    return render(request, "sign_up.html")

def logout(request):
    auth.logout(request)
    return redirect('/')