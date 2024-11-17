from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class Program(models.Model):
    program_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255) 
    amount = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return(f'{self.program_name} - {self.short_name} - {self.amount} {self.created}')
    

class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(default='profile/wbm-logo.png', upload_to='profile')
    program = models.ManyToManyField(Program, blank=True)
    # add additional fields in here

    def __str__(self):
        return self.username