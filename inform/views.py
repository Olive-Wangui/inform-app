from django.shortcuts import render
import datetime as dt
from .models import *

# Create your views here.
def index(request):
    date = dt.date.today()
    # business = Business.get_allbusiness()
    all_neighborhoods = Neighbourhood.get_neighbourhoods()
    
    
    if 'neighbourhood' in request.GET and request.GET["neighbourhood"]:
        neighbourhoods = request.GET.get("neighbourhood")
        searched_neighbourhood = Business.get_by_neighbourhood(neighbourhoods)
        all_posts = Post.get_by_neighbourhood(neighbourhoods)
        message = f"{neighbourhoods}"
        all_neighbourhoods = Neighbourhood.get_neighborhoods()        
        
        return render(request, 'index.html', {"message":message,"location": searched_neighbourhood,
                                               "all_neighbourhoods":all_neighbourhoods, "all_posts":all_posts})

    else:
        message = "No Neighbourhood Found!"

    return render(request, 'index.html', {"date": date, "all_neighborhoods":all_neighborhoods,})