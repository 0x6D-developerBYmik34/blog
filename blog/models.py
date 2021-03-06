from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
    """docstring for Post
    models.ForeignKey -- 
    связь многие(много Post.objects)-к-одному(auth.User)
    """

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
        