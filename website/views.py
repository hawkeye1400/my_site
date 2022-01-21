from django.shortcuts import render 


def index_view(request):
    return render(request, 'website\index.htm')

def about_view(request):  
    return render(request, r'website\about.htm')  

def contact_view(request):
    return render(request, 'website\contact.htm') 

