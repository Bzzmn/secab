from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'wagtail/news/home_page.html')
