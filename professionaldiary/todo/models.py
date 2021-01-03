from django.db import models

# Create your models here.

class Task(models.Model):

    status_choices= (
        ('O','Over'),
        ('C','Current'),
        ('U','Upcoming')
    )

    # can change this to
    # status_choices=(
    #     ('O','Completed'),
    #     ('C',"OnGoing"),
    #     ('U','Later')
    # )


    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100,blank=True,null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=1, choices=status_choices,null=True)

    

    def __str__(self):
        return f'{self.title},{self.id}'
