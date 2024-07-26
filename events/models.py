from django.db import models

# Create your models here.

class Event(models.Model):
       name = models.CharField(max_length=255)
       date = models.DateTimeField()
       location = models.CharField(max_length=255)
       description = models.TextField(blank=True)

       def __str__(self):
           return self.name