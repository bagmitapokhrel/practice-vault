from django.contrib import admin
from .models import Category,Destination, Package, Booking, Tour, Gallery, Payment, TripInquiry

# Register your models here.
admin.site.register(Category)
admin.site.register(Destination)
admin.site.register(Package)
admin.site.register(Booking)
admin.site.register(Tour)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'destination', 'image', 'description')
    search_fields = ('title', 'destination__name')  # Allow searching by title and destination name
    list_filter = ('destination',)  # Add a filter for destination



@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        "booking",
        "amount",
        "payment_method",
        "status",
        "transaction_id",
        "created_at",
    )

    list_filter = (
        "payment_method",
        "status",
    )

    search_fields = (
        "transaction_id",
    )



@admin.register(TripInquiry)
class TripInquiryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "destination",
        "travel_date",
        "travelers",
        "budget",
        "fitness_level",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "fitness_level",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "destination__name",
    )

    ordering = (
        "-created_at",
    )

from django.contrib import admin
from .models import Guide, GuideBooking


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "location",
        "specialization",
        "experience",
        "daily_rate",
        "rating",
        "verified",
        "available",
    )

    list_filter = (
        "specialization",
        "experience",
        "verified",
        "available",
    )

    search_fields = (
        "name",
        "location",
        "languages",
    )

    list_editable = (
        "verified",
        "available",
    )


@admin.register(GuideBooking)
class GuideBookingAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "guide",
        "start_date",
        "end_date",
        "number_of_people",
        "total_amount",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "start_date",
        "guide",
    )

    search_fields = (
        "user__username",
        "user__email",
        "guide__name",
    )
