from django.contrib import admin
from .models import Category,Destination, Package, Booking, Tour, Gallery

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

