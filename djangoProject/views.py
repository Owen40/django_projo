from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def comp(request):
    return render(request, 'components.html')