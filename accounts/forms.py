
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'username',
            'placeholder': 'Username',
            'id': 'username'
        })
    )
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'password',
        'placeholder': 'password',
        'id': 'password'
    }))


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label='First name',
        max_length=30,
        widget=forms.TextInput(attrs={
            'class':'inputjon',
            'placeholder': 'Ism*',
            'name':'name'
        })
    )
    last_name = forms.CharField(
        label = 'Last name',
        max_length=30,
        widget=forms.TextInput(attrs={
            'class':'inputjon',
            'placeholder': 'Familiya*',
            'name':'surname'
        })
    )
    username = forms.CharField(
        label = 'Username',
        max_length=30,
        widget=forms.TextInput(attrs={
            'class':'inputjon',
            'placeholder': 'Username*',
            'name':'username'
        })
    )
    email = forms.EmailField(
        label = 'Email',
        max_length=30,
        widget=forms.TextInput(attrs={
            'class':'inputjon',
            'placeholder': 'Email*',
            'name':'email'
        })
    )
    password= forms.CharField(
        label = 'Password',
        max_length=30,
        widget=forms.PasswordInput(attrs={
            'class':'inputjon',
            'placeholder': 'Password*',
            'name':'password'
        })
    )
    password_check= forms.CharField(
        label = 'Password confirm',
        max_length=30,
        widget=forms.PasswordInput(attrs={
            'class':'inputjon',
            'placeholder': 'Passwordni qayta kiriting*',
            'name':'password_check'
        })
    )