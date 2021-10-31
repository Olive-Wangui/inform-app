from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.http import Http404

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    occupants_count = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    def save_neighbourhood(self):
        self.save()
    
    def delete_neighbourhood(self):
        self.delete()
        
    @classmethod
    def get_neighbourhoods(cls):
        projects = cls.objects.all()
        return projects
    
    @classmethod
    def search_neighbourhoods(cls, search_term):
        projects = cls.objects.filter(name__icontains=search_term)
        return projects
    
    
    @classmethod
    def get_by_admin(cls, Admin):
        projects = cls.objects.filter(Admin=Admin)
        return projects
    
    
    @classmethod
    def get_neighborhood(request, neighborhood):
        try:
            project = Neighbourhood.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return project
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Neighborhood'
        verbose_name_plural = 'Neighborhoods'
