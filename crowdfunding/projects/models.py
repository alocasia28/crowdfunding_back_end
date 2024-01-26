from django.db import models
from django.contrib.auth import get_user_model 
from django.db.models import Sum
#note: you can't just import USER in this because not recommended because "of a quirk in the way django handles users"

# Create your models here.
User = get_user_model()


class Project(models.Model):
    CATEGORIES = {
    ('Hydro', 'Hydroponics'),
    ('Container', ' Container Gardening'),
    ('Raised', 'Raised Beds'),
    ('Indoor', 'Indoor Gardens'),
    ('No', 'No Category')

    }

    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    total = models.IntegerField(default=0, null=True, blank=True)
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    categories = models.CharField(max_length=100,choices=CATEGORIES, default="No Category")
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        related_name='owned_projects'
    )
    def update_total(self, project_id):
        pledges = Pledge.objects.filter(project_id=project_id)
        self.total = pledges.aggregate(Sum('amount'))['amount__sum']
        self.save()

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
        User,
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )

class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="comments")
    body = models.TextField()
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name="comments")
    visible = models.BooleanField(default=True)

    
    