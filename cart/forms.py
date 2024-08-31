from django import forms

class CheckoutForm(forms.Form):
    CARD_CHOICES = [
        ('credit', 'Credit Card'),
        ('debit', 'Debit Card'),
    ]
    card_type = forms.ChoiceField(choices=CARD_CHOICES, label='Card Type')
    card_number = forms.CharField(max_length=16, label='Card Number')
    expiration_date = forms.CharField(max_length=5, label='Expiration Date (MM/YY)')
    cvv = forms.CharField(max_length=3, label='CVV')