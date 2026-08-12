from django import forms
from adminpage.models import Booking

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            "full_name",
            "email",
            "phone",
            "number_of_people",
            "travel_date",
            "special_requests",
        ]

        widgets = {

            "full_name": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lux",
                    "placeholder": "Your full name",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control form-control-lux",
                    "placeholder": "you@example.com",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lux",
                    "placeholder": "+977 98XXXXXXXX",
                }
            ),

            "number_of_people": forms.NumberInput(
                attrs={
                    "class": "form-control form-control-lux",
                    "min": 1,
                }
            ),

            "travel_date": forms.DateInput(
                attrs={
                    "class": "form-control form-control-lux",
                    "type": "date",
                }
            ),

            "special_requests": forms.Textarea(
                attrs={
                    "class": "form-control form-control-lux",
                    "rows": 4,
                    "placeholder": "Any special requests?",
                }
            ),
        }