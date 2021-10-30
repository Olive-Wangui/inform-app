from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    occupants_count = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)