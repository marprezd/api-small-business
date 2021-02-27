# api-small-business/accounts/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    """This class extends UserCreationForm and extends the base form. 

    Args:
        UserCreationForm ([type]): [description]
    """
    class Meta:
        model = get_user_model()  # Our CustomUser model
        fields = ('email', 'username',)
        

class CustomUserChangeForm(UserChangeForm):
    """This class extends UserChangeForm and allows a registered user
    can change your email and username.

    Args:
        UserChangeForm ([type]): [description]
    """
    class Meta:
        model = get_user_model()  # Our CustomUser model
        fields = ('email', 'username',)