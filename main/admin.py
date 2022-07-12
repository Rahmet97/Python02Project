from django.contrib.auth.models import User, Group
from django.contrib import admin
from .models import Project, Form

admin.site.register((Project, Form))
admin.site.unregister((User, Group))
