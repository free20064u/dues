from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField 
from pilkit.processors import ResizeToFill


# Create your models here.
# Program studeid by students
class Program(models.Model):
    program_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255) 
    amount = models.DecimalField(max_digits=60,decimal_places=2,default=0.00)
    created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return(f'{self.program_name} - {self.created.strftime("%Y")}')
      
# iformation about users of the app
class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    program = models.ManyToManyField(Program)
    is_staff = models.BooleanField(blank=True, default=False)
    is_superuser = models.BooleanField(blank=True, default=False)
    is_active = models.BooleanField(blank=True, default=True)
    image = ProcessedImageField(blank=True, null=True,default='profile/wbm-logo.png', upload_to='profile',processors=[ResizeToFill(100, 100)],format='JPEG',options={'quality': 60})


    def imageURL(self):
        if self.image == None:
            return '/medial/profile/wbm-logo.png'
        else:
            return self.image.url

    def __str__(self):
        return self.username

