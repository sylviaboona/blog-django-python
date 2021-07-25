from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# class RegisterUser(CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/register_user.html'
#     success_url = reverse_lazy('login-user')


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        return redirect('login-user')
    return render(request, 'registration/register_user.html')
# 

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            # send a message to the user trying to login
            return render(request, 'registration/login_user.html')
        login(request, user)
        return redirect('all-articles-url')
    return render(request, 'registration/login_user.html')

def logout_user(request):
        logout(request)
        return redirect('all-articles-url')

