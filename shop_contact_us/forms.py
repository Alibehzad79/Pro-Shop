from django import forms
from django.core import validators


class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Please enter your full name", "class": "form-control"}),
        label="Full Name",
        validators=[
            validators.MaxLengthValidator(200, "Your name could not be more than 200 characters")
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Please enter your email", "class": "form-control"}),
        label="Email",
        validators=[
            validators.EmailValidator()
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Please enter your subject", "class": "form-control"}),
        label="Subject",
        validators=[
            validators.MaxLengthValidator(500, "Your subject could not be more than 500 characters")
        ]
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Please enter your message", "class": "form-control"}),
        label="Message"
    )
