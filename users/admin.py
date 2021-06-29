from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomChangeForm, CustomCreationForm


class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    list_display = ['username', 'email']
    add_form = CustomCreationForm
    form = CustomChangeForm

admin.site.register(get_user_model(), CustomUserAdmin)