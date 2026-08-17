from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from adminpage.models import Gallery, Category, Destination, Package, Booking, Tour, Review, Payment, GearItem, Wishlist
from .forms import BookingForm, GearChecklistForm
from django.contrib.auth.decorators import login_required

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


def search(request):

    query = request.GET.get("q", "").strip()

    packages = Package.objects.none()
    destinations = Destination.objects.none()

    if query:
        packages = Package.objects.filter(
            title__icontains=query
        )

        destinations = Destination.objects.filter(
            name__icontains=query
        )

    context = {
        "query": query,
        "packages": packages,
        "destinations": destinations,
    }

    return render(
        request,
        "userpage/search.html",
        context
    )

def package(request):

    packages = Package.objects.all()

    wishlist_package_ids = set()

    if request.user.is_authenticated:

        wishlist_package_ids = set(
            Wishlist.objects.filter(
                user=request.user
            ).values_list(
                "package_id",
                flat=True
            )
        )

    return render(
        request,
        "userpage/packages.html",
        {
            "packages": packages,
            "wishlist_package_ids": wishlist_package_ids
        }
    )

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

def contact(request):
    return render(request, "userpage/contact.html")

def review(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'userpage/review.html', context)

def gallery(request):
    galleries = Gallery.objects.all()   
    context = {
        'galleries': galleries,
    }
    return render(request, 'userpage/gallery.html', context)

def booking(request, package_id):

    package = get_object_or_404(
        Package,
        id=package_id
    )

    if request.method == "POST":

        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            # Attach the selected package
            booking.package = package

            # Get number of people
            number_of_people = booking.number_of_people

            # Check minimum
            if number_of_people < 1:

                messages.error(
                    request,
                    "You must book for at least one guest."
                )

                return redirect(
                    "package_detail",
                    package_id=package.id
                )

            # Check maximum capacity
            if (
                package.max_people
                and number_of_people > package.max_people
            ):

                messages.error(
                    request,
                    f"Maximum {package.max_people} guests "
                    f"are allowed for this package."
                )

                return redirect(
                    "package_detail",
                    package_id=package.id
                )

            # Calculate total price
            booking.price = (
                package.price * number_of_people
            )

            # Save booking
            booking.save()

            messages.success(
                request,
                "Your booking has been successfully submitted! "
                "We will contact you shortly."
            )

            return redirect(
                "package_detail",
                package_id=package.id
            )

    else:

        form = BookingForm()

    context = {
        "package": package,
        "form": form,
    }

    return render(
        request,
        "userpage/package_detail.html",
        context
    )


def payment(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    if request.method == "POST":

        payment_method = request.POST.get(
            "payment_method"
        )

        if payment_method not in ["esewa", "cod"]:

            messages.error(
                request,
                "Please select a payment method."
            )

            return redirect(
                "payment",
                booking_id=booking.id
            )

        payment = Payment.objects.create(

            booking=booking,

            amount=booking.package.price,

            payment_method=payment_method,

            status="pending"

        )

        if payment_method == "cod":

            payment.status = "pending"

            payment.save()

            return redirect(
                "payment_success",
                payment_id=payment.id
            )

        if payment_method == "esewa":

            # For now we create the payment record.
            # eSewa Sandbox will be connected next.

            return redirect(
                "payment_success",
                payment_id=payment.id
            )


    return render(
        request,
        "userpage/payment.html",
        {
            "booking": booking
        }
    )


def gear_checklist(request):

    gear_items = []

    if request.method == "POST":

        form = GearChecklistForm(request.POST)

        if form.is_valid():

            season = form.cleaned_data["season"]
            altitude = form.cleaned_data["altitude"]
            difficulty = form.cleaned_data["difficulty"]

            gear_items = GearItem.objects.filter(
                min_altitude__lte=altitude
            ).filter(
                difficulty__in=[
                    "easy",
                    difficulty
                ]
            )

            gear_items = [
                item for item in gear_items
                if item.season in ["all", season]
            ]

    else:

        form = GearChecklistForm()

    return render(
        request,
        "userpage/gear_checklist.html",
        {
            "form": form,
            "gear_items": gear_items,
        }
    )

def travel_map(request):
    destinations = Destination.objects.exclude(
        latitude__isnull=True,
    ).exclude(
        longitude__isnull=True
    )

    return render(
        request,
        "userpage/travel_map.html",
        {
            "destinations": destinations
        }
    )



@login_required
def add_to_wishlist(request, package_id):

    package = get_object_or_404(
        Package,
        id=package_id
    )

    wishlist_item = Wishlist.objects.filter(
        user=request.user,
        package=package
    ).first()

    if wishlist_item:
        # Already in wishlist → remove it
        wishlist_item.delete()

    else:
        # Not in wishlist → add it
        Wishlist.objects.create(
            user=request.user,
            package=package
        )

    return redirect(
        request.META.get(
            "HTTP_REFERER",
            "package"
        )
    )

@login_required
def remove_from_wishlist(request, package_id):

    Wishlist.objects.filter(
        user=request.user,
        package_id=package_id
    ).delete()

    return redirect(
        request.META.get(
            "HTTP_REFERER",
            "wishlist"
        )
    )


@login_required
def wishlist(request):

    wishlists = Wishlist.objects.filter(
        user=request.user
    ).select_related("package", "package__destination")

    return render(
        request,
        "userpage/wishlist.html",
        {
            "wishlists": wishlists
        }
    )

