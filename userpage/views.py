from django.shortcuts import render
from adminpage.models import Category, Destination

# Create your views here.
def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'userpage/index.html', context)

