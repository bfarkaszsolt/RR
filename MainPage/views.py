

from django.shortcuts import render
from django.utils import timezone
from .models import PosttoMainPage

def index(request):

    return render(request, 'MainPage/masolat.html')