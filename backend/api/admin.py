from django.contrib import admin

# 自作UserをAdminに設定
from django.contrib.auth.admin import UserAdmin
from .models import User


admin.site.register(User, UserAdmin)

