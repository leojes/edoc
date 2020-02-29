from django.db import models

# Create your models here.
class Projects(models.Model):
    project =models.CharField(max_length=100)
    description = models.TextField()
    button = models.Button()