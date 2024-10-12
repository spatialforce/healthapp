from .views import register, Home, clinics_search, home_page,wards_search, hospital_search,about_page,wards_page,hos_page,web_map,custom_login_view
from django.urls import path

urlpatterns = [
    path("", Home.as_view(), name='home_url'),
    path("clinics/", clinics_search, name='clinics_url'),
    path("wards/", wards_search, name='wards_url'),  
    path('hospitals/', hospital_search, name='hospitals_url'),
    path('register/', register, name='register_url'),
    path('About us/',about_page,name='about_url'),
    path('whome/', wards_page,name='whome'),
    path('hhome/',hos_page,name='hhome'),
    path('homee/',home_page,name='homepage_url'),
    path('webmap/',web_map,name='webmap_url'),
    path('login/',custom_login_view, name='login_url')
    
]
