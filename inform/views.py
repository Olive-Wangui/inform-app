from django.shortcuts import render, redirect, HttpResponseRedirect
import datetime as dt
from .models import *
from .forms import * 
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth import logout as django_logout

# Create your views here.
def index(request):
    date = dt.date.today()
    # business = Business.get_allbusiness()
    all_neighbourhoods = Neighbourhood.get_neighbourhoods()
    
    
    if 'neighbourhood' in request.GET and request.GET["neighbourhood"]:
        neighbourhoods = request.GET.get("neighbourhood")
        searched_neighbourhood = Business.get_by_neighbourhood(neighbourhoods)
        all_posts = Post.get_by_neighbourhood(neighbourhoods)
        message = f"{neighbourhoods}"
        all_neighbourhoods = Neighbourhood.get_neighbourhoods()        
        
        return render(request, 'index.html', {"message":message,"location": searched_neighbourhood,
                                               "all_neighbourhoods":all_neighbourhoods, "all_posts":all_posts})

    else:
        message = "No Neighbourhood Found!"

    return render(request, 'index.html', {"date": date, "all_neighbourhoods":all_neighbourhoods,})

login_required(login_url='/accounts/login/')
def profile(request, username):
    return render(request, 'profile.html')

def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateProfileForm(instance=request.user.profile)
    
    return render(request, 'editprofile.html', {'user_form': user_form, 'prof_form': prof_form})
    
login_required(login_url='/accounts/login/')
def search_businesses(request):
    if 'keyword' in request.GET and request.GET['keyword']:
        search_term = request.GET.get('keyword')
        searched_projects = Business.search_business(search_term)
        message = f"(search_term)"
        
        return render(request, 'search.html', {"message": message, "businesses": searched_projects})
    else:
        message = "No business searched"
        return render(request, 'search.html', {"message": message})
    

def get_business(request, id):

    try:
        project = Business.objects.get(pk = id)
        
    except ObjectDoesNotExist:
        raise Http404()
    
    
    return render(request, "projects.html", {"project": project})
    
login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    profile = request.user.profile
    
    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.Admin = current_user
            project.admin_profile = profile
            project.save()
        return redirect('index')

    else:
        form = NewBusinessForm()
    return render(request, 'new-business.html', {"form": form})

@login_required
def logout(request):
    django_logout(request)
    return  HttpResponseRedirect('/')

    
login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    profile = request.user.profile
    neighbourhood = request.user.profile.neighbourhood

    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Author = current_user
            post.author_profile = profile
            post.neighbourhood = neighbourhood
            post.save()
        return redirect('index')

    else:
        form = NewPostForm()
    return render(request, 'new-post.html', {"form": form})