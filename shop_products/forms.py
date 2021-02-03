from django import forms
from django.core import validators


class ProductCommentForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Please enter your name.", "class": "form-control"}),
        label="Name",
        validators=[
            validators.MaxLengthValidator(200, "Your name could not be more than 200 characters.")
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Please enter your email.", "class": "form-control"}),
        label="Email",
        validators=[
            validators.EmailValidator()
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Please enter your text.", "class": "form-control"}),
        label="Text"
    )

    productId = forms.IntegerField(
        widget=forms.HiddenInput()
    )
