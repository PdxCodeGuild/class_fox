from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Note)

# OR ------

#from .models import Note
#admin.site.register(Note)