from django.contrib import admin
from .models import UserProfile


# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    pass
    # list_display = ['name', 'email', 'address', 'nick_name']


admin.site.register(UserProfile, UserProfileAdmin)
