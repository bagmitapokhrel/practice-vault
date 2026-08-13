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

from django import forms


class GearChecklistForm(forms.Form):

    SEASON_CHOICES = [
        ("spring", "Spring"),
        ("summer", "Summer"),
        ("autumn", "Autumn"),
        ("winter", "Winter"),
    ]

    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("moderate", "Moderate"),
        ("difficult", "Difficult"),
    ]

    ALTITUDE_CHOICES = [
        (2000, "Below 2,000 m"),
        (4000, "2,000 – 4,000 m"),
        (5500, "4,000 – 5,500 m"),
        (6000, "Above 5,500 m"),
    ]

    season = forms.ChoiceField(
        choices=SEASON_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-select"
            }
        )
    )

    altitude = forms.IntegerField(
        label="Maximum Altitude",
        widget=forms.Select(
            choices=ALTITUDE_CHOICES,
            attrs={
                "class": "form-select"
            }
        )
    )

    difficulty = forms.ChoiceField(
        choices=DIFFICULTY_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-select"
            }
        )
    )