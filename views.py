from django.shortcuts import render, redirect
from .models import Clinics, Wards, Hospitals
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.serializers import serialize
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


class Home(TemplateView):
 template_name = 'homepage.html'


def register(request):
  
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login_url') 
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})

  
def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage_url')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")  
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})
   

def clinics(request):
 clinics_json = serialize('geojson', Clinics.objects.all())
 return HttpResponse(clinics_json, content_type='application/json')


def wards(request):
 wards_json = serialize('geojson', Wards.objects.all())
 return HttpResponse(wards_json, content_type='application/json')

def hospitals(request):
 hos_json=serialize('geojson',Hospitals.objects.all())
 return HttpResponse(hos_json,content_type=('application/json'))

def hospital_search(request):
 query=request.GET.get('q')
 if query:
    result= Hospitals.objects.filter(name_icontains=query)
 else:
   result= Hospitals.objects.all()    

 searched= serialize('geojson', result)  
 return HttpResponse(searched,content_type='/applicaton/json')

def wards_search(request):
 query=request.GET.get('q')
 if query:
    result=Wards.objects.filter(admin3name_icontains=query)
 else:
   result=Wards.objects.all()
 searched= serialize('geojson',result)   
 return HttpResponse(searched,content_type='application/json')

def clinics_search(request):
 query= request.GET.get('q')

 if query:
    result= Clinics.objects.filter(name_icontains=query)
 else:
    result=Clinics.objects.all()
    
 searched= serialize('geojson', result)
 return HttpResponse(searched,content_type='application/json')


def about_page(request):
    return render(request, 'contact_page.html')

def wards_page(request):
  return render(request, 'wards.html')

def hos_page(request):
  return render(request, 'hospitals.html')
def home_page(request):
  return render(request,'homepage.html')
def web_map(request):
  return render(request, 'webmap.html')






