from django.shortcuts import render, redirect
from .forms import BookingForm

def home(request):
    
    return render(request, 'index.html')