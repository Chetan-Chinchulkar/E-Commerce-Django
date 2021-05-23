from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Items(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    #rating=models.FloatField(validators=2)
    rating=models.IntegerField()
    quantity=models.IntegerField()
    category=models.CharField(max_length=10)
    unq_id=models.IntegerField(unique=True)
    #date_sold=models.DateTimeField(default=timezone.now)
    #feedback=models.TextField(blank=True)
    imgscr=models.URLField(blank=True)
    #site_own=models.URLField(blank=True)

    def __str__(self):
        return self.name

