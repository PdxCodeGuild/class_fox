from django.db import models

class Link(models.Model):
    url = models.CharField(max_length=1000)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    counter = models.IntegerField(default=0)
    last_visited = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.url