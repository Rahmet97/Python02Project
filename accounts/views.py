from distutils.command.clean import clean
from multiprocessing import context
from re import template
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth.hashers import make_password, check_password


class LoginView(View):
    template_name = 'login.html'
    initial = { 'key' : 'value' }
    form_class = LoginForm
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        self.context['loginForm'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        try:
            form = self.form_class(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = User.objects.get(username=username)
                print(user)
                if check_password(password, user.password):
                    auth.login(request, user)
                    return redirect('/')
                else:
                    messages.error(request, "Username or password is invalid!")
                    return redirect('login')
        except User.DoesNotExist:
            messages.error(request, "Username or password is invalid!")
            return redirect('login')


class RegisterView(View):
    template_name = 'sign_up.html'
    initial = {'key': 'value'}
    form_class = RegisterForm
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        self.context['RegisterForm']= form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            surname = form.cleaned_data["surname"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            password_check = form.cleaned_data["password_check"]

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
        else:
            return redirect('register')


def logout(request):
    auth.logout(request)
    return redirect('/')