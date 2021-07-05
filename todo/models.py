from django.db import models

# Create your models here.
class TodoItem(models.Model):
  content = models.CharField(max_length=9)

class TodoCep(models.Model):
  content = models.CharField(max_length=9)