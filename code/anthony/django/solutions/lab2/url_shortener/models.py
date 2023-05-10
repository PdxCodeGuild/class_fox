from django.db import models

class Link(models.Model):
    url = models.URLField(unique=True)
    code = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now_add => sets current date/time when Link is created
    # auto_now => sets current date/time when Link is created or updated
    counter = models.IntegerField(default=0)
    last_visited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"({self.code}) -- {self.url}" # (ABH122) -- https://google.com