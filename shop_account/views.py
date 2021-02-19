from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, DetailView

from shop_account.forms import LoginForm, RegisterForm, EditProfileForm, MyChangeFormPassword, EditUser
from django.contrib.auth import login, logout, authenticate

from shop_account.models import UserProfile


def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    login_form = LoginForm(request.POST or None)

    if login_form.is_valid():
        user_name = login_form.cleaned_data.get("user_name")
        password = login_form.cleaned_data.get("password")

        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            messages.success(request, "You have been logged in successfully.")
            login(request, user)
            return redirect("/")
        else:
            login_form.add_error("user_name", "Username or password is incorrect.")
    context = {
        "login_form": login_form
    }
    return render(request, "account/login_page.html", context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        user_name = register_form.cleaned_data.get("user_name")
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")
        new_user = User.objects.create_user(username=user_name, email=email, password=password)
        UserProfile.objects.create(user=new_user)
        if new_user is not None:
            messages.success(request, "You have successfully registered.")
            return redirect("/login")
        else:
            messages.error(request, "There was an error registering you.")
            register_form.add_error('user_name',
                                    "The username or email you entered will not be valid. Please change your username or email.")
    context = {
        "register_form": register_form
    }
    return render(request, "account/register_page.html", context)


def log_out(request):
    logout(request)
    return redirect("/login")


@login_required(login_url="/login")
def user_panel(request, *args, **kwargs):
    user = request.user
    return render(request, "account/user_panel.html", {"user": user})


@login_required(login_url="/login")
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        user_form = EditUser(instance=user, data=request.POST)
        profile_form = EditProfileForm(instance=user.userprofile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "profile update successfully!")
        else:
            messages.error(request, "profile updating failed!")
    else:
        user_form = EditUser(instance=user)
        profile_form = EditProfileForm(instance=user.userprofile)

    return render(request, "account/edit_profile.html", {"user_form": user_form, "profile_form": profile_form})


@login_required(login_url="/login")
def edit_password(request):
    user_id = request.user.id
    user: User = User.objects.get(id=user_id)
    form_change_password = MyChangeFormPassword(request.POST or None)
    if form_change_password.is_valid():
        password = form_change_password.cleaned_data.get("password")
        user.set_password(raw_password=password)
        user.save()
        return redirect("/user-panel")
    context = {
        "form_edit_password": form_change_password
    }
    return render(request, "account/edit_password.html", context)
