from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Board, Board_content, CustomUser, Post

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age',)}),)
    list_display = ['username', 'email', 'age']

admin.site.register(CustomUser, UserAdmin)

admin.site.register(Post)
admin.site.register(Board)
admin.site.register(Board_content)