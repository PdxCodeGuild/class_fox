from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from posts.models import Post
import requests
import random


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Delete all users except admin
        User.objects.exclude(is_superuser=True).delete()

        # get 10 users from jsonplaceholder
        # https://jsonplaceholder.typicode.com/users
        # https://jsonplaceholder.typicode.com/posts

        users = requests.get(
            'https://jsonplaceholder.typicode.com/users').json()
        posts = requests.get(
            'https://jsonplaceholder.typicode.com/posts').json()

        # Create users
        for user in users:
            User.objects.create_user(
                username=user['username'],
                email=user['email'],
                password='123456'
            )

        User.objects.create_superuser(
            username='testUser',
            password='123456',
        )

        users = User.objects.all()
        # Create posts
        for post in posts:
            Post.objects.create(
                title=post['title'],
                content=post['body'],
                author=User.objects.get(pk=random.choice(users).pk)
            )
