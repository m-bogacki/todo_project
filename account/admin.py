from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.




class AdminUser(BaseUserAdmin):
    pass


admin.site.register(User, AdminUser)