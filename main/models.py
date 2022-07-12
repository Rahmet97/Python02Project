from tabnanny import verbose
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="pictures")

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

class Form(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    project_description = models.TextField()

    class Meta:
        verbose_name = "Request"
        verbose_name_plural = "Requests"

    def __str__(self):
        return self.full_name