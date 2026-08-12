from django.shortcuts import render, redirect
from .forms import PackageForm, DestinationForm
from django.contrib import messages
from .models import Destination, Package, Booking
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required




# Create your views here.
@staff_member_required(login_url="/adminpage/login/")
def PackageCreateView(request):
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Package created successfully!")
            return redirect('package_create')
        else:
            messages.error(request, "There was an error creating the package. Please check the form for errors.")
            return render(request, 'adminpage/package_form.html', {'form': form})
    else:
        form = PackageForm()
    
    return render(request, 'adminpage/package_form.html', {'form': form})

@staff_member_required(login_url="/adminpage/login/")
def DestinationCreateView(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Destination created successfully!")
            return redirect('destination_create')
        else:
            messages.error(request, "There was an error creating the destination. Please check the form for errors.")
            return render(request, 'adminpage/destination_form.html', {'form': form})
    else:
        form = DestinationForm()
    
    return render(request, 'adminpage/destination_form.html', {'form': form})


from .forms import TravelPlanForm

@staff_member_required(login_url="/adminpage/login/")
def travel_plan(request):

    if request.method == "POST":

        form = TravelPlanForm(request.POST)

        if form.is_valid():

            plan = form.save(commit=False)

            if request.user.is_authenticated:
                plan.user = request.user

            plan.save()

            messages.success(
                request,
                "Travel plan created successfully!"
            )

            return redirect("travel_plan")

    else:

        form = TravelPlanForm()

    return render(
        request,
        "adminpage/travel_plan.html",
        {
            "form": form
        },
    )

@staff_member_required(login_url="/adminpage/login/")
def admin_dashboard(request):

    context = {
        "destinations_count": Destination.objects.count(),
        "packages_count": Package.objects.count(),
        "bookings_count": Booking.objects.count(),
        "users_count": User.objects.count(),
    }

    return render(
        request,
        "adminpage/dashboard.html",
        context
    )


def admin_login(request):

    if request.user.is_authenticated:
        return redirect("admin_dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            # Only allow staff/admin users
            if user.is_staff:

                login(request, user)

                return redirect("admin_dashboard")

            else:

                messages.error(
                    request,
                    "You do not have permission to access the admin dashboard."
                )

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

    return render(
        request,
        "adminpage/login.html"
    )

@staff_member_required(login_url="/adminpage/login/")
def admin_logout(request):

    logout(request)

    return redirect("admin_login")

@staff_member_required(login_url="/adminpage/login/")
def bookings(request):

    bookings = Booking.objects.all()
    cancelled_count = Booking.objects.filter(
    status__iexact="Cancelled"
).count()
    pending_count = Booking.objects.filter(
    status__iexact="Pending"
).count()
    confirmed_count = Booking.objects.filter(
    status__iexact="Confirmed"
).count()

    context = {
        "bookings": bookings,
        "cancelled_count": cancelled_count,
        "pending_count": pending_count,
        "confirmed_count": confirmed_count
    }

    return render(
        request,
        "adminpage/booking.html",
        context
    )

@staff_member_required(login_url="/adminpage/login/")
def booking_edit(request, booking_id):

    booking = Booking.objects.get(id=booking_id)

    if request.method == "POST":

        status = request.POST.get("status")

        if status in ["pending", "confirmed", "cancelled"]:

            booking.status = status
            booking.save()

            messages.success(
                request,
                "Booking status updated successfully."
            )

        else:

            messages.error(
                request,
                "Invalid status value."
            )

        return redirect("bookings")

    context = {
        "booking": booking
    }

    return render(
        request,
        "adminpage/booking_edit.html",
        context
    )