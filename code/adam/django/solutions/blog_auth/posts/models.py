from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_at']


"""
EXPLANATIONS:

author field:
1. We import the User model from django.contrib.auth.models.
2. We add an author field to the Post model.
3. We use the ForeignKey field to define a one-to-many relationship.
This means that a user can have multiple posts but a post can only have one user.
4. We use the on_delete=models.CASCADE argument which specifies the behavior
when the referenced object is deleted.
This is called a CASCADE delete meaning that when a User is deleted,all the posts created by that user will also be deleted.

get_absolute_url method:
1. We import reverse from django.urls, which allows us to generate the URLs
by reversing the URL patterns of the app
2. We add a get_absolute_url method to the Post model.
This method will return the URL string of the post.
3. In the next line, we tell Django to use the 'post-detail' URL pattern
defined in blog/urls.py. This pattern has the name 'post-detail'
and the URL will be like 'post/<int:pk>/' where pk stands for "Primary Key"
which is a unique key for each post.
4. Finally, we pass the 'pk' argument to the reverse function to specify
which post we want the URL for. pk is the primary key or the id of the post.
5. When we create a new post, Django will redirect us to the post-detail
page of the newly created post.
For this to work, we need to add a get_absolute_url method to the Post model
as shown above.

class Meta:
1. The class Meta is used to define metadata about the model.
2. ordering = ['-created_at'] is used to sort the data in descending order of the created_at field."""
