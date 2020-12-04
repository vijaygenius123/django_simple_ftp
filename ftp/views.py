from django.shortcuts import render
from os import listdir
# Create your views here.

def home(request):
    files = listdir('./files')
    return render(request, 'ftp/home.html', {'files': files})