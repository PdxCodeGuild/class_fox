from django.contrib import admin
from .models import Type, Ability, Pokemon

admin.site.register([Type, Ability, Pokemon])
