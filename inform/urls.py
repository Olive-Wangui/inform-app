from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/edit', views.edit_profile, name='edit'),
]