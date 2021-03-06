from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.forms import TextInput, EmailInput, NumberInput, ImageField, URLInput

from shop_account.models import UserProfile


class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")
        widgets = {
            'first_name': TextInput(attrs={'class': "form-control"}),
            'last_name': TextInput(attrs={'class': "form-control"}),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("age", "about_me", "web_site", "image")
        widgets = {
            'age': NumberInput(attrs={'class': "form-control"}),
            'about_me': TextInput(attrs={'class': "form-control"}),
            'web_site': URLInput(attrs={'class': "form-control"}),
            # class="profile-image-inner-container bg-color-primary"
        }


class MyChangeFormPassword(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Please Enter your Password", "class": "form-control form-control"}),
        label="Password",
        validators=[
            validators.MinLengthValidator(6, "The password can not be less than 6 characters."),
            validators.MaxLengthValidator(12, "The password can not be more than 12 characters.")
        ]
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Please Enter your Password again", "class": "form-control form-control"}),
        label="Password again"
    )

    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        if password != re_password:
            raise forms.ValidationError("Passwords are different.")
        return password


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Please Enter your UserName", "class": "form-control form-control-lg"}),
        label="Username"
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Please Enter your Password", "class": "form-control form-control-lg"}),
        label="Password"
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")
        is_exists = User.objects.filter(username=user_name).exists()
        if not is_exists:
            raise forms.ValidationError("Username or password is incorrect.")

        return user_name


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Please Enter your UserName", "class": "form-control form-control-lg"}),
        label="Username",
        validators=[
            validators.MinLengthValidator(3, "Username can not be less than 3 characters."),
            validators.MaxLengthValidator(12, "Username can not be more than 12 characters.")
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "Please Enter your E-mail Address", "class": "form-control form-control-lg"}),
        label="E-mail Address",
        validators=[
            validators.EmailValidator("The entered email is invalid.")
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Please Enter your Password", "class": "form-control form-control-lg"}),
        label="Password",
        validators=[
            validators.MinLengthValidator(6, "The password can not be less than 6 characters."),
            validators.MaxLengthValidator(12, "The password can not be more than 12 characters.")
        ]
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Please Enter your Password again", "class": "form-control form-control-lg"}),
        label="Password again"
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")
        is_exists = User.objects.filter(username=user_name).exists()
        if is_exists:
            raise forms.ValidationError(
                "The username or email you entered will not be valid. Please change your username or email.")
        return user_name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            raise forms.ValidationError(
                "The username or email you entered will not be valid. Please change your username or email.")
        return email

    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        if password != re_password:
            raise forms.ValidationError("Passwords are different.")
        return password
