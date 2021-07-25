from django.urls import path
# from .views import RegisterUser
from . import views


# app_name = 'writers'
urlpatterns = [
    path('register/', views.register_user, name='register-user'),
     path('login/', views.login_user, name='login-user'),
     path('logout', views.logout_user, name='logout-user'),
    # path('register/', RegisterUser.as_view(), name='register-user'), # our-domain.com/meetups
    # path('login/', ArticlesList.as_view(), name='login-user'),
    # path('logout', ArticleDetail.as_view(), name='logout-user'),
    
]