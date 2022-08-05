import django
from django.contrib import admin
from links import models
# Register your models here.
admin.site.register(models.Link)