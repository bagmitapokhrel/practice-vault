from django.forms import ModelForm
from adminpage.models import Package, Booking, Destination


class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = '__all__'

class DestinationForm(ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'  
