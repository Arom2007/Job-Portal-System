from django.db import models
from django.contrib.auth.models import User
from commons.models import BaseModel

class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=14)
    resume = models.FileField(null=True, blank=True, upload_to="resumes")
    profile_picture = models.FileField(null=True, blank=True, upload_to="profile_pictures")


class UserAccountActivationKey(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=50)

