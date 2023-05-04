from django.db import models

# Create your models here.
# url
# code
# created_at

class Link(models.Model):
    url = models.CharField(max_length=100)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.url
