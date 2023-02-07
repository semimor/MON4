from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from users.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
# Create your views here.

def login_view(request):
    if request.method == 'GET':
        context = {
            'form': LoginForm

        }
        return render(request, 'users/login.html', context=context)


    if request.method=='POST':
        form = LoginForm(data=request.POST)
        """authenticate user"""

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('/products')
            else:
                form.add_error('username', 'еще раз(')

        return render(request, 'users/login.html', context={
            'form':form
        })

def logout_view(request):
    logout(request)
    return redirect('/products/')


def register_view(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm
        }
        return render(request, 'users/register.html', context=context)

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            password1, password2 = form.cleaned_data.get('password1'), form.cleaned_data.get('password2')
            if password1 == password2:
                User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )
                return redirect('/users/login/')
            else:
                form.add_error('password1', 'дагы бир жолу)')


        return render(request, 'users/register.html', context={
                'form': form
        })


# class CustomForm:
#
#     def __init__(self, data):
#         self.data = data
#
#
#     @property
#     def validate_data(self) -> bool:
#         if self.data == '':
#             return True
#
#
#
#
# print(CustomForm(data={}).validate_data)



