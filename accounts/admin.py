# # api-small-business/accounts/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    """This class extends from UserAdmin. Use the model and custom user forms.

    Args:
        UserAdmin ([type]): [description]
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]
    
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)