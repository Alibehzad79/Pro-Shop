from django import forms
from django.core import validators


class BlogCommentForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Please enter your full name", "class": "form-control"}),
        label="Full Name",
        validators=[
            validators.MaxLengthValidator(200, "Your name could not be more than 200 characters")
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Please enter your email", "class": "form-control"}),
        label="Email"
    )

    comment = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Please enter your comment", "class": "form-control"}),
        label="Comment"
    )

    blog_id = forms.IntegerField(
        widget=forms.HiddenInput()
    )
