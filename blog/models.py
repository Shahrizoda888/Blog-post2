from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
from django.db import models
# from django.utils.html import escape,make_safe
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import AbstractUser,User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=300)
    body=models.TextField()
    author=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    ),
    created_at=models.DateTimeField(auto_now=True)
    objects= models.Manager()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.pk)])

