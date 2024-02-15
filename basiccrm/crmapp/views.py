from django.shortcuts import render

def index(request):
    return render(request, 'src/index.html')

def about(request):
    return render(request, 'src/about.html')