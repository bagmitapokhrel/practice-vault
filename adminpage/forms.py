from django.forms import ModelForm
from adminpage.models import Package, Booking, Destination, Tour


class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = '__all__'

class DestinationForm(ModelForm):
    class Meta:
        model = Destination
        fields = '__all__' 

class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'

from django import forms
from .models import TravelPlan

class TravelPlanForm(forms.ModelForm):

    class Meta:
        model = TravelPlan
        fields = [
            "destination",
            "travel_date",
            "travelers",
            "budget",
            "hotel",
            "transport",
            "meals",
            "special_requests",
        ]

        widgets = {
            "travel_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),

            "travelers": forms.NumberInput(
                attrs={
                    "min": 1,
                    "class": "form-control"
                }
            ),

            "budget": forms.NumberInput(
                attrs={
                    "placeholder": "Enter your budget",
                    "class": "form-control"
                }
            ),

            "special_requests": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Special requests..."
                }
            ),
        }        




