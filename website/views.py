from django.shortcuts import render 
from django.http import HttpResponse, JsonResponse

def index_view(request):
    return render(request, 'website\index.htm')

def about_view(request):  
    return render(request, r'website\about.htm')  

def contact_view(request):
    return render(request, 'website\contact.htm') 