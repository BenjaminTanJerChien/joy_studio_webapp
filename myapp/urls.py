from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name = "index"),
    path('register', views.register, name = "register"),
    path('login', views.login, name = "login"),
    path('logout', views.logout, name = "logout"),
    path('profile', views.profile, name="profile"),
    path('profile/update', views.profile_update, name = "profile_update"),
    path('post/<str:pk>', views.post, name="post"),
    path('calc', views.calc, name="calc"),
    path('change_password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='templates/change_password_done.html'), 
        name='password_change_done'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='templates/change_password.html'), 
        name='password_change'),
    path('reset_password/done/', auth_views.PasswordResetCompleteView.as_view(template_name='templates/reset_password_done.html'),
     name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='templates/reset_password_complete.html'),
     name='reset_password_complete'),
    
   
    
    
    ]

