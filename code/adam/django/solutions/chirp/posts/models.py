from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author
    
    def url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    class Order:
        order = ['-created_at']
