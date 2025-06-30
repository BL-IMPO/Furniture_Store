from django import forms


class CreateOrderFrom(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField()
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField()

    # The bad way to store data like this because we will be involved in frontend part
    #first_name = forms.CharField(
    #    widget=forms.TextInput(
    #        attrs={
    #            "class": "form-control",
    #            "placeholder": "Wpisz swoje imię",
    #        }
    #    )
    #)
#
    #last_name = forms.CharField(
    #    widget=forms.TextInput(
    #        attrs={
    #            "class": "form-control",
    #            "placeholder": "Wpisz swoje nazwistko",
    #        }
    #    )
    #)
#
    #phone_number = forms.CharField(
    #    widget=forms.TextInput(
    #        attrs={
    #            "class": "form-control",
    #            "placeholder": "Numer telefonu",
    #        }
    #    )
    #)
#
    #requires_delivery = forms.ChoiceField(
    #    widget=forms.RadioSelect(),
    #    choices=[
    #        ("0", False),
    #        ("1", True),
    #    ]
    #)
#
    #delivery_address = forms.CharField(
    #    widget=forms.Textarea(
    #        attrs={
    #            "class": "form-control",
    #            "id": "delivery-address",
    #            "rows": 2,
    #            "placeholder": "Wprowadź adres wysyłki",
    #        }
    #    )
    #)
#
    #payment_on_get = forms.ChoiceField(
    #    widget=forms.RadioSelect(),
    #    choices=[
    #        ("0", 'False'),
    #        ("1", 'True'),
    #    ],
    #    initial="card"
    #)

