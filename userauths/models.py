import string

from django.db import models
from django.contrib.auth.models import AbstractUser

from shortuuid.django_fields import ShortUUIDField
# Create your models here.

GENDER = (
    ("Female", "Female"),
    ("Male", "Male"),
    ("Other", "Other"),
)

IDENTITY_TYPE = (
    ("National Identification Number", "National Identification Number"),
    ("Driver's License", "Driver's License"),
    ("International Passport", "International Passport"),
)

def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (instance.user.id, filename)
    return "user_{0}/{1}".format(instance.user.id, filename)

class User(AbstractUser):
    full_name = models.CharField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=500, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, default="Other")

    otp = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = ['email']
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.full_name


class Profile(models.Model):
    pid = ShortUUIDField(Length=7, max_length=25, alphabets="abcdefghijklmnopqrstuvwxyz123")
    image = models.FileField(upload_to=user_directory_path, default="default.jpg", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, default="Other")

    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)

    identity_type = models.CharField(max_length=20, choices=IDENTITY_TYPE, null=True, blank=True)