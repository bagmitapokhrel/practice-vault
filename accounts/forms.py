from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=100,
        required=True
    )

    last_name = forms.CharField(
        max_length=100,
        required=True
    )

    email = forms.EmailField(
        required=True
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control form-control-lux",
            })




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = [
            "profile_picture",
            "phone",
            "location",
        ]

        widgets = {
            "profile_picture": forms.ClearableFileInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "+977 98XXXXXXXX"
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Kathmandu, Nepal"
                }
            ),
        }