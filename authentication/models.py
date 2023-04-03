from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'
    
    ROLE_CHOICES = ((CREATOR, 'Creator'), 
                    (SUBSCRIBER, 'Subscriber'),)
    profile_photo = models.ImageField(upload_to="media/",blank=True)
    role =models.CharField(max_length=30, choices=ROLE_CHOICES)
    
    def set_profile_picture(self):
        pic = self.profile_photo
        if not pic:
            self.profile_photo="media/Image_1.jpg"
    