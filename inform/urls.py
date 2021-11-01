from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/edit', views.edit_profile, name='edit'),
    path('search/', views.search_businesses, name='search_results'),
    path('business/(\d+)', views.get_business, name='business_results'),
    path('new/business', views.new_business, name='new_business'),
    path('new/post', views.new_post, name='new_post'),
    path('logout/', views.logout, name='logout'),
    path('accounts/profile/', LoginView.as_view(template_name='profile.html'), name='profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)