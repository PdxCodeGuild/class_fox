# Generated by Django 4.2 on 2023-05-06 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0002_link_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='last_visited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
