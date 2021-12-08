from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_creator = models.BooleanField(default = False, verbose_name='content creator')
    is_adult = models.BooleanField(default = False, verbose_name='over 18')
    date_of_birth = models.DateField(null=True, blank=True)
    website = models.URLField(blank=True)
    biography = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='static/images', null=True, blank=True)

    def __str__(self):
        return self.username