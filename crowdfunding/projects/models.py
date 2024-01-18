from django.db import models
from django.contrib.auth import get_user_model 
#note: you can't just import USER in this because not recommended because "of a quirk in the way django handles users"

# Create your models here.

class Project(models.Model):
    # def sum_pledges(pk):
    #     sum = 0
    #     for n in Pledge.models:
    #         if Pledge.project == pk:
    #             sum = sum + Pledge.amount
    #     return sum
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    # total = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, 
        related_name='owned_projects'
    )


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )

    
    