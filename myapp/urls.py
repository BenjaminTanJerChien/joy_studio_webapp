from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView


urlpatterns = [
    path('', views.index, name = "index"),
    path('register', views.register, name = "register"),
    path('login', views.login, name = "login"),
    path('logout', views.logout, name = "logout"),
    path('profile', views.profile, name="profile"),
    path('profile/update', views.profile_update, name = "profile_update"),
    path('post/<str:pk>', views.post, name="post"),
    path('calc', views.calc, name="calc"),
    path('profile/change-password', views.change_password, name ="change_password"),
    
   
    
    
    ]

