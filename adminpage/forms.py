from django.forms import ModelForm
from adminpage.models import Package, Booking, Destination, Tour, TripInquiry, TravelPlan


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




class TripInquiryForm(forms.ModelForm):

    class Meta:
        model = TripInquiry

        fields = [
            "destination",
            "travel_date",
            "travelers",
            "duration",
            "fitness_level",
            "budget",
            "preferred_region",
            "special_requests",
        ]

        widgets = {

            "destination": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "travel_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "travelers": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                    "placeholder": "Number of travelers",
                }
            ),

            "duration": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                    "placeholder": "Number of days",
                }
            ),

            "fitness_level": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "budget": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0,
                    "step": "0.01",
                    "placeholder": "Your approximate budget",
                }
            ),

            "preferred_region": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Annapurna, Everest, Pokhara",
                }
            ),

            "special_requests": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Tell us about your preferences, requirements, or special requests...",
                }
            ),
        }    




