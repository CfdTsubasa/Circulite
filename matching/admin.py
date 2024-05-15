from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    ordering = ('id',)  # ユーザーモデルの存在するフィールドに変更
    list_display = ('id' , 'name', 'email', 'is_active', 'is_staff')  # name を追加
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('name',)}),
    )
    # ここで extra_fields は実際にモデルに存在するフィールド名に置き換えてください

admin.site.register(User, CustomUserAdmin)