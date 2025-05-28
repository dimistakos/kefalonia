from django.shortcuts import render

from userauths.models import User, Profile
from userauths.forms import UserRegisterForm
# Create your views here.


def RegisterView(request):
    form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, "userauths/sign-up.html", context)