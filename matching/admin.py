from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from matching.models import  Interest, UserInterest , CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    ordering = ('id',)  # ユーザーモデルの存在するフィールドに変更
    list_display = ('id' , 'name', 'email', 'is_active', 'is_staff','bio','date_joined')  # name を追加
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('name',)}),
    )
    # ここで extra_fields は実際にモデルに存在するフィールド名に置き換えてください

class UserInterestAdmin(admin.ModelAdmin):
    model = UserInterest
    ordering = ('id',)  # ユーザーモデルの存在するフィールドに変更
    list_display = ('id','interest','user')

# admin.site.register(CustomUser, UserAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Interest)
admin.site.register(UserInterest,UserInterestAdmin)
