from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from adminpage.models import Gallery, Category, Destination, Package, Booking, Tour, Review
from .forms import BookingForm
# Create your views here.
def index(request):
    packages = Package.objects.all()
    categories = Category.objects.all()
    destinations = Destination.objects.all()
    bookings = Booking.objects.all()

    context = {
        'packages' : packages,
        'categories': categories,
        'destinations': destinations,
        'bookings' : bookings,
    }
    return render(request, 'userpage/index.html', context)

def package(request):
    packages = Package.objects.all()
    context = {
        'packages': packages,
    }
    return render(request, 'userpage/packages.html', context)

def package_detail_view(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.package = package
            booking.save()
            messages.success(request, "Your booking has been successfully submitted! We will contact you shortly.")
            return redirect('package_detail', package_id=package.id)
    else:
        form = BookingForm()
        
    context = {
        'package': package,
        'form': form,
    }
    return render(request, 'userpage/package_detail.html', context)

def destination(request):
    destinations = Destination.objects.all()
    context = {
        'destinations': destinations,
    }
    return render(request, 'userpage/destination.html', context)

def destination_detail(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id) # id =3
    context = {
        'destination': destination,
    }
    return render(request, 'userpage/destination_detail.html', context)

def tour(request):
    tours = Tour.objects.all()
    context = {
        'tours': tours,
    }
    return render(request, 'userpage/tour.html', context)

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    
    context = {
        'tour': tour,
    }
    return render(request, 'userpage/tour_detail.html', context)

def review(request):
    return render(request, 'userpage/review.html')

def about(request):
    return render(request, "userpage/about.html")

def gallery(request):
    galleries = Gallery.objects.all().order_by("-uploaded_at")  # Order by uploaded_at in descending order
    context = {
        'galleries': galleries,
    }
    return render(request, 'userpage/gallery.html', context)