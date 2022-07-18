from django.contrib import admin
from .models import Project, Form

admin.site.register((Project, Form))
