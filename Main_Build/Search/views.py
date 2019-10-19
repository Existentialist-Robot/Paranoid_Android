from django.http import HttpResponse
from django.shortcuts import render #, redirect, get_object_or_404
from .models import People #Paper, Product
#from django.db.models import Q


# Create your views here.

def home(request): # going to have to include the search parameters here as a form
    return render(request,'search/search_home.html')
#    return HttpResponse("Hello, world. You're at the home page.")

def search_list(request):
    return render(request,'search/search_list.html')
    
def people_list(request):
    peoples = People.objects.all().order_by('date')
    return render(request,'search/people_list.html', {'peoples':peoples})

def people_detail(request, slug):
    people = People.objects.get(slug=slug)
    return render(request, 'search/people_detail.html',{'people':people})
    return HttpResponse(slug)

def mission(request):
    return render(request,'search/search_mission.html')

#    return render(request,'search/misson_list.html')
    
def contact(request):
    return render(request,'search/search_contact.html')
