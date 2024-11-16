from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(default='profile/wbm-logo.png', upload_to='profile')
    #program = models.ManyToManyField(Program, blank=True, null=True, default=1)
    # add additional fields in here

    def __str__(self):
        return self.username