from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.
# class RegisterUser(CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/register_user.html'
#     success_url = reverse_lazy('login-user')

def user_must_be_logged_out_to_access(user):
    return not user.is_authenticated
def user_must_be_superuser(user):
    return user.is_superuser
    
@user_passes_test(user_must_be_logged_out_to_access, login_url='/list/', redirect_field_name=None)
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        if not username:
            return render(request, 'registration/register_user.html', {'usernameErr':'username is empty'})
        email = request.POST['email']
        if not email:
            return render(request, 'registration/register_user.html')
        password = request.POST['password']
        if not password:
            return render(request, 'registration/register_user.html')
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

@login_required
def logout_user(request):
    logout(request)
    return redirect('all-articles-url')

# def user_must_be_logged_out_to_access(user):
    # return not user.is_authenticated

# @user_passes_test(user_must_be_logged_out_to_access, login_url='/', redirect_field_name=None)