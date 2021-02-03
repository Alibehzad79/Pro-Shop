from django import forms


class OrderDetailForm(forms.Form):
    productId = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    count = forms.IntegerField(
        widget=forms.NumberInput(),
        initial=1
    )
