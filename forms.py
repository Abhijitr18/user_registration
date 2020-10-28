from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


from .models import Profile_Reg


class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields =['email','password1','password2','first_name','last_name']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile_Reg
        fields = ['address', 'city', 'post']