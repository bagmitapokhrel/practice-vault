from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from adminpage.models import Gallery, Category, Destination, Package, Booking, Tour, Review, Payment, GearItem, Wishlist, Guide, GuideBooking
from .forms import BookingForm, GearChecklistForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime

# Create your views here.
def index(request):
    destinations = Destination.objects.all()
    packages = Package.objects.all()

    context = {
        "destinations": destinations,
        "packages": packages,
    }

    return render(request, "userpage/index.html", context)


from django.db.models import Q

def search(request):

    query = request.GET.get("q", "").strip()

    packages = Package.objects.none()
    destinations = Destination.objects.none()

    if query:

        packages = Package.objects.filter(
            Q(title__icontains=query) 
        ).distinct()

        destinations = Destination.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query)
        ).distinct()

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


def trip_builder_success(request):

    return render(
        request,
        "userpage/trip_builder_success.html"
    )

def guides(request):

    guides = Guide.objects.filter(
        available=True
    ).order_by(
        "-verified",
        "-rating"
    )

    context = {
        "guides": guides,
    }

    return render(
        request,
        "userpage/guides.html",
        context
    )

def guide_detail(request, guide_id):

    guide = get_object_or_404(
        Guide,
        id=guide_id
    )

    context = {
        "guide": guide,
    }

    return render(
        request,
        "userpage/guide_detail.html",
        context
    )

@login_required
def guide_booking(request, guide_id):

    guide = get_object_or_404(
        Guide,
        id=guide_id,
        available=True
    )

    if request.method == "POST":

        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        number_of_people = request.POST.get(
            "number_of_people"
        )
        message = request.POST.get("message")

        if not start_date or not end_date:

            messages.error(
                request,
                "Please select both start and end dates."
            )

            return redirect(
                "guide_booking",
                guide_id=guide.id
            )

        try:

            start = datetime.strptime(
                start_date,
                "%Y-%m-%d"
            ).date()

            end = datetime.strptime(
                end_date,
                "%Y-%m-%d"
            ).date()

        except ValueError:

            messages.error(
                request,
                "Invalid date selected."
            )

            return redirect(
                "guide_booking",
                guide_id=guide.id
            )

        if start < timezone.localdate():

            messages.error(
                request,
                "Start date cannot be in the past."
            )

            return redirect(
                "guide_booking",
                guide_id=guide.id
            )

        if end < start:

            messages.error(
                request,
                "End date cannot be before the start date."
            )

            return redirect(
                "guide_booking",
                guide_id=guide.id
            )

        try:
            people = int(number_of_people)
        except (TypeError, ValueError):

            people = 1

        if people < 1:
            people = 1

        number_of_days = (
            end - start
        ).days + 1

        total_amount = (
            guide.daily_rate *
            number_of_days
        )

        booking = GuideBooking.objects.create(

            user=request.user,

            guide=guide,

            start_date=start,

            end_date=end,

            number_of_people=people,

            message=message,

            total_amount=total_amount,

            status="Pending"
        )

        messages.success(
            request,
            "Your guide booking request has been submitted."
        )

        return redirect(
            "guide_booking_success",
            booking_id=booking.id
        )

    context = {
        "guide": guide,
    }

    return render(
        request,
        "userpage/guide_booking.html",
        context
    )

@login_required
def guide_booking_success(request, booking_id):

    booking = get_object_or_404(
        GuideBooking,
        id=booking_id,
        user=request.user
    )

    return render(
        request,
        "userpage/guide_booking_success.html",
        {
            "booking": booking
        }
    )

def travel_quiz(request):

    return render(
        request,
        "userpage/travel_quiz.html"
    )


from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q

from adminpage.models import Package, Destination


from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q

from adminpage.models import Package, Destination


@require_POST
def travel_assistant(request):

    message = request.POST.get("message", "").strip()

    if not message:
        return JsonResponse({
            "success": False,
            "message": "Tell me where you want to go, your budget, duration, or travel style."
        })

    text = message.lower()

    # =========================================================
    # 1. DETECT DIFFICULTY
    # =========================================================

    difficulty = None

    if any(word in text for word in [
        "easy",
        "beginner",
        "first trek",
        "first time",
        "relaxed",
        "family friendly"
    ]):
        difficulty = "Easy"

    elif any(word in text for word in [
        "moderate",
        "medium",
        "average"
    ]):
        difficulty = "Moderate"

    elif any(word in text for word in [
        "hard",
        "difficult",
        "challenging",
        "experienced",
        "advanced",
        "extreme"
    ]):
        difficulty = "Hard"


    # =========================================================
    # 2. DETECT DESTINATION / REGION
    # =========================================================

    destinations = [
        "everest",
        "annapurna",
        "langtang",
        "mustang",
        "pokhara",
        "kathmandu",
        "chitwan",
        "manaslu",
        "tilicho",
        "mardi",
        "upper mustang",
        "lower mustang",
        "bandipur",
        "lumbini",
        "paris",
        "dubai",
        "bali",
        "thailand",
        "bangkok",
        "phuket",
        "istanbul",
        "venice",
        "athens",
        "maldives",
        "santorini"
    ]

    detected_destination = None

    for destination in destinations:

        if destination in text:
            detected_destination = destination
            break


    # =========================================================
    # 3. DETECT TRAVEL STYLE
    # =========================================================

    travel_style = None

    if any(word in text for word in [
        "trek",
        "trekking",
        "hiking",
        "mountain"
    ]):
        travel_style = "trekking"

    elif any(word in text for word in [
        "beach",
        "sea",
        "island",
        "relax"
    ]):
        travel_style = "beach"

    elif any(word in text for word in [
        "culture",
        "historical",
        "history",
        "temple"
    ]):
        travel_style = "culture"

    elif any(word in text for word in [
        "adventure",
        "adventurous",
        "rafting",
        "extreme"
    ]):
        travel_style = "adventure"

    elif any(word in text for word in [
        "family",
        "kids",
        "children"
    ]):
        travel_style = "family"


    # =========================================================
    # 4. DETECT BUDGET
    # =========================================================

    budget = None

    import re

    numbers = re.findall(
        r'\d+(?:,\d+)*(?:\.\d+)?',
        text
    )

    if numbers:

        try:
            budget = float(
                numbers[0].replace(",", "")
            )
        except ValueError:
            budget = None


    # =========================================================
    # 5. BUILD PACKAGE QUERY
    # =========================================================

    query = Q()

    has_filter = False


    # ---------------------------------------------------------
    # Destination filter
    # ---------------------------------------------------------

    if detected_destination:

        query |= Q(
            title__icontains=detected_destination
        )

        query |= Q(
            destination__name__icontains=detected_destination
        )

        has_filter = True


    # ---------------------------------------------------------
    # Difficulty filter
    # ---------------------------------------------------------

    if difficulty:

        query &= Q(
            difficulty__iexact=difficulty
        )

        has_filter = True


    # ---------------------------------------------------------
    # Travel style
    # ---------------------------------------------------------

    if travel_style == "trekking":

        query |= Q(
            title__icontains="trek"
        )

        query |= Q(
            title__icontains="hiking"
        )

        query |= Q(
            title__icontains="mountain"
        )

        has_filter = True


    elif travel_style == "beach":

        query |= Q(
            title__icontains="beach"
        )

        query |= Q(
            title__icontains="island"
        )

        has_filter = True


    elif travel_style == "culture":

        query |= Q(
            title__icontains="culture"
        )

        query |= Q(
            title__icontains="heritage"
        )

        has_filter = True


    elif travel_style == "adventure":

        query |= Q(
            title__icontains="adventure"
        )

        query |= Q(
            title__icontains="rafting"
        )

        has_filter = True


    # =========================================================
    # 6. GET RECOMMENDATIONS
    # =========================================================

    if has_filter:

        recommendations = Package.objects.filter(
            query
        ).distinct()[:6]

    else:

        recommendations = Package.objects.all()[:6]


    # =========================================================
    # 7. IF NOTHING FOUND
    # =========================================================

    if not recommendations:

        recommendations = Package.objects.all()[:3]

        response_message = (
            "I couldn't find an exact match for that request yet. "
            "Here are a few popular journeys you might like."
        )

    else:

        first = recommendations[0]

        response_message = (
            f"✨ I found some journeys that match your preferences. "
            f"My top suggestion is **{first.title}**."
        )


    # =========================================================
    # 8. PACKAGE DATA
    # =========================================================

    package_data = []

    for package in recommendations:

        package_data.append({

            "id": package.id,

            "title": package.title,

            "price": str(package.price),

            "difficulty": package.difficulty,

            "duration": package.duration,

        })


    # =========================================================
    # 9. PERSONALIZED RESPONSE
    # =========================================================

    preferences = []

    if detected_destination:
        preferences.append(
            detected_destination.title()
        )

    if difficulty:
        preferences.append(
            difficulty
        )

    if travel_style:
        preferences.append(
            travel_style
        )


    if preferences:

        response_message += (
            " I considered: "
            + ", ".join(preferences)
            + "."
        )


    return JsonResponse({

        "success": True,

        "message": response_message,

        "packages": package_data,

    })

