from django import forms
from adminpage.models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone', 'number_of_people', 'travel_date', 'special_requests']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-0 py-2', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-dark text-white border-0 py-2', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-0 py-2', 'placeholder': 'Phone Number'}),
            'number_of_people': forms.NumberInput(attrs={'class': 'form-control bg-dark text-white border-0 py-2', 'min': 1, 'value': 1}),
            'travel_date': forms.DateInput(attrs={'class': 'form-control bg-dark text-white border-0 py-2', 'type': 'date'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control bg-dark text-white border-0 py-2', 'rows': 3, 'placeholder': 'Any special requirements?'}),
        }