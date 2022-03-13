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
    path('profile/reset-password', PasswordResetView.as_view(), name ="reset_password"),
    path('profile/reset-password/done', PasswordResetDoneView.as_view(), name="password_reset_done"),
    """path(r'^profile/reset-password/confirm/(?P<uid>[0-9A-Za-z]+)-(?P<token>.+)/$', #used regular expresssion idk wth this even means
    PasswordResetConfirmView.as_view(), name="password_reset_confirm"), 
    path()"""
    
    
    ]

