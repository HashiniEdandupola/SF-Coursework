from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def facilities(request):
    return render(request, 'main/facilities.html')