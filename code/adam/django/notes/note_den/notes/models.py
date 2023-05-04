from django.db import models

# Create your models here.
CHOICES = [
   # ('stored in db', 'human readable',)
    ('I', 'Important'),
    ('U', 'Urgent'),
    ('T', 'Todo'),
    ('L', 'Lesson Note'),

]

class Note(models.Model):
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(choices=CHOICES, max_length=1, 
                           blank=True, null=True)
    
    def __str__(self):
        return f"{self.tag} -- {self.title}"