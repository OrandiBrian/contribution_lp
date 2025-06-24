from django import forms 

class PaymentForm(forms.Form):
    full_name = forms.CharField(label='Full Name',
                                required=True,
                                max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': 'Enter full name', 'class': 'input input-bordered w-full'}))
    phone_number = forms.CharField(max_length=15, 
                                   required=True, 
                                   label='Phone Number',
                                   widget=forms.TextInput(attrs={'placeholder': '2547XXXXXXXX',
                                                                #  'pattern': '^(\+254|0)[17]\\d{8}$',
                                                                 'class': 'input input-bordered w-full'}))
    amount = forms.IntegerField(min_value=1, 
                                required=True, 
                                label='Amount',
                                widget=forms.NumberInput(attrs={'placeholder': 'Enter amount',
                                                                'class': 'input input-bordered w-full'}))