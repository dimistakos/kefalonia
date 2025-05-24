from django import forms
from django.contrib.auth.forms import UserCreationForm

from userauths.models import User, Profile

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'password1', 'password2']