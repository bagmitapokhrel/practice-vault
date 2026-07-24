from django.forms import ModelForm
from adminpage.models import Package, Booking


class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = '__all__'