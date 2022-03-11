from django.contrib import admin
from .models import Title, Post, Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Registered models here.
admin.site.register(Title)
admin.site.register(Post)

class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = "Acccount"

class CustomUser (UserAdmin):
    inlines = (AccountInline, )

admin.site.unregister(User)
admin.site.register(User, CustomUser)