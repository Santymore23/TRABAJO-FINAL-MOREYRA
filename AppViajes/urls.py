from django.urls import path
from AppViajes import views

urlpatterns = [
    path('AppViajes/',include('AppViajes.urls')),
]