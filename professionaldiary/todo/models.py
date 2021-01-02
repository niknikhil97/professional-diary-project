from django.db import models

# Create your models here.

class Task(models.Model):

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100,blank=True,null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.title},{self.id}'
