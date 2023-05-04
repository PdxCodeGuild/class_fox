from django.contrib import admin
from .models import Note

# Register your models here.
admin.site.register(Note)


# --- OR ----
# from . import models
# admin.site.register(models.Note)
