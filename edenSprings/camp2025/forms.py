from django import forms 

class PaymentForm(forms.Form):
    phone_number = forms.CharField(max_length=15, required=True, label='Phone Number')
    amount = forms.IntegerField(min_value=1, required=True, label='Amount')