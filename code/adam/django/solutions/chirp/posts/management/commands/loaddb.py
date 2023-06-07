from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from posts.models import Post
import requests
import random


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.exclude(is_superuser=True).delete()


        users = requests.get(
            'https://jsonplaceholder.typicode.com/users').json()
        posts = requests.get(
            'https://jsonplaceholder.typicode.com/posts').json()
        
        for user in users:
            User.objects.create_user(
                username = user['username'],
                email = user['email'],
                password = 'chirper'
            )

        User.objects.create_superuser(
            username = 'testUser',
            password = '123456'
        )

        users = User.objects.all()
        for post in posts:
            Post.objects.create(
                content = post['body'],
                author = User.objects.get(pk=random.choice(users).pk)
            )