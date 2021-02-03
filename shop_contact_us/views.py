from django.shortcuts import render, redirect

# Create your views here.
from shop_contact_us.forms import ContactUsForm
from shop_contact_us.models import ContactUs
from shop_settings.models import Setting, SocialNetwork, BusinessHours


def contact_us(request):
    setting = Setting.objects.first()
    networks = SocialNetwork.objects.all()
    business_hours = BusinessHours.objects.all()
    contact_us_form = ContactUsForm(request.POST or None)

    if contact_us_form.is_valid():
        full_name = contact_us_form.cleaned_data.get("full_name")
        email = contact_us_form.cleaned_data.get("email")
        subject = contact_us_form.cleaned_data.get("subject")
        message = contact_us_form.cleaned_data.get("message")

        new_contact = ContactUs.objects.create(full_name=full_name, email=email, subject=subject, message=message)
        if new_contact is not None:
            return redirect("/contact-us")
        contact_us_form = ContactUsForm()

    context = {
        "contact_us_form": contact_us_form,
        "setting": setting,
        'networks': networks,
        "business_hours": business_hours
    }
    return render(request, "contact_us/contact_us.html", context)
