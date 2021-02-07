from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from shop_account.forms import LoginForm, RegisterForm, EditProfileForm, MyChangeFormPassword
from django.contrib.auth import login, logout, authenticate


def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    login_form = LoginForm(request.POST or None)

    if login_form.is_valid():
        user_name = login_form.cleaned_data.get("user_name")
        password = login_form.cleaned_data.get("password")

        user = authenticate(request, username=user_name, password=password)
        if user is not None:
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
        if new_user is not None:
            return redirect("/login")
        else:
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
    user_id = request.user.id
    context = {}
    return render(request, "account/user_panel.html", context)


@login_required(login_url="/login")
def edit_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    edit_form = EditProfileForm(request.POST or None,
                                initial={"first_name": user.first_name, "last_name": user.last_name})
    if edit_form.is_valid():
        first_name = edit_form.cleaned_data.get("first_name")
        last_name = edit_form.cleaned_data.get("last_name")

        user.first_name = first_name
        user.last_name = last_name
        user.save()

    context = {
        "edit_form": edit_form
    }
    return render(request, "account/edit_profile.html", context)


@login_required(login_url="/login")
def edit_password(request):
    user_id = request.user.id
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
