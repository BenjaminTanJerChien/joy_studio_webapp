from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('register', views.register, name = "register"),
    path('login', views.login, name = "login"),
    path('logout', views.logout, name = "logout"),
    path('profile', views.profile, name="profile"),
    path('profile/update', views.profile_update, name = "profile_update"),
    path('post/<str:pk>', views.post, name="post"),
    path('calc', views.calc, name="calc")
    
]

