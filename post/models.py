from django.conf import settings
from django.db import models


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='post')
    content = models.TextField()
    modify_date = models.DateTimeField('Modify Date', auto_now=True)


    def __str__(self):
        return self.owner

    class Meta:
        ordering = ['-modify_date']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',  on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    content = models.TextField()


    def __str__(self):
        return self.owner
