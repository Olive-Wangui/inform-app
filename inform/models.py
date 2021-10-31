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
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    picture = models.ImageField(upload_to = 'profile_pics/', blank=True, default='profile_pics/default.jpg')
    neighbourhood = models.ForeignKey('Neighbourhood', on_delete=models.CASCADE, blank=True, default='1')
    
    
    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()