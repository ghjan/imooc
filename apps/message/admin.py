from django.contrib import admin
from .models import UserMessage


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'address', 'message']


admin.site.register(UserMessage, UserMessageAdmin)
