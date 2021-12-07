from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'is_creator', 'is_adult', 'date_of_birth']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_creator', 'is_adult', 'date_of_birth',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2', 'is_creator', 'is_adult', 'date_of_birth',)}),
    )
    

admin.site.register(CustomUser, CustomUserAdmin)