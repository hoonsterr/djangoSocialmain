from django.contrib import admin
from .models import Document
from django.contrib.auth import get_user_model


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_nick', 'user_pw', 'user_email')


admin.site.register(Document)