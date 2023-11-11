from django.shortcuts import render
from .models import Vacansies
# Create your views here.

def main(request):
    return render(request, 'main/index.html')

def vacansies(request):
    vacansies = Vacansies.objects.all()
    return render(request, 'main/index.html', context={'vacansies':vacansies})