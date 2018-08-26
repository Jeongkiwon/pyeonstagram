from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_superuser(self, *args, **kwargs):
        return super().create_superuser( *args, **kwargs)


class User(AbstractUser):
    img_profile = models.ImageField(upload_to='user', blank=True)
    like_posts = models.ManyToManyField('post.Post', blank=True, related_name='like_users')
    user_id =models.CharField(unique=True,blank=False,max_length=15)

    name=models.CharField( max_length=30)
    description = models.TextField(blank=True)
    objects = UserManager()

    def __str__(self):
        return self.username