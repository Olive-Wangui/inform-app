from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
 
 
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email')
        

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'picture', 'neighbourhood']
        
class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['Admin', 'pub_date', 'admin_profile']
        widgets = {
          'address': forms.Textarea(attrs={'rows':1, 'cols':10,}),
        }

class NewNeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['Admin', 'pub_date', 'admin_profile']
        
        
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['Author', 'pub_date', 'author_profile', 'neighbourhood']
        widgets = {
          'post': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }
