from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
# Create your models here.


class CustomUser(AbstractUser):
    pass



class Chef(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="chef")
    background = models.TextField()
    speciality = models.CharField(max_length=200)

    




@receiver(post_save, sender=CustomUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)