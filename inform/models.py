from django.db import models
from django.contrib.auth.models import User
from django.http import Http404
from django.db.models.signals import post_save
from django.dispatch import  receiver
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=250)
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
    def get_neighbourhood(request, neighborhood):
        try:
            project = Neighbourhood.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return project
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Neighbourhood'
        verbose_name_plural = 'Neighbourhoods'
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pics/', blank=True, default='profile_pics/default.jpg')
    neighbourhood = models.ForeignKey('Neighbourhood', on_delete=models.SET_NULL, null=True, related_name='occupant', blank=True)
    
    def __str__(self):
        return f'{self.user.username} profile'
    
    def delete(self):
        self.delete()
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
class Business(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    admin_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, default='1')
    address = models.TextField()
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE, blank=True, default='1')
     
     
    def save_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()
        
    @classmethod
    def get_allbusiness(cls):
        business = cls.objects.all()
        return business
    
    @classmethod
    def search_business(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business
    
    @classmethod
    def get_by_neighbourhood(cls, neighbourhoods):
        business = cls.objects.filter(neighbourhood__name__icontains=neighbourhoods)
        return business
    
    @classmethod
    def get_businesses(request, id):
        try:
            business = Business.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return business
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'My Business'
        verbose_name_plural = 'Business'

class Post(models.Model):
    post = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    
    def save_post(self):
        self.save()
    
    def delete_post(self):
        self.delete()
        
    @classmethod
    def get_allpost(cls):
        posts = cls.objects.all()
        return posts
    
    @classmethod
    def get_by_neighbourhood(cls, neighbourhoods):
        posts = cls.objects.filter(neighbourhood__name__icontains=neighbourhoods)
        return posts
    
    def __str__(self):
        return self.post
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Post'
        verbose_name_plural = 'Posts'