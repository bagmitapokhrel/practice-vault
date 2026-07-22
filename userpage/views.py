from django.shortcuts import render
from adminpage.models import Category, Destination, Package

# Create your views here.
def index(request):
    packages = Package.objects.all()
    categories = Category.objects.all()
    destinations = Destination.objects.all()

    context = {
        'packages' : packages,
        'categories': categories,
        'destinations': destinations,
    }
    return render(request, 'userpage/index.html', context)

