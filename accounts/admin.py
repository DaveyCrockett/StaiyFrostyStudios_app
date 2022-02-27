from pyexpat import model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "department", "role", "is_staff", "email"]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("department", "role")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("department", "role")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)