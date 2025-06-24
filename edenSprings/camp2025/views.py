from django.shortcuts import render
from .forms import PaymentForm
from dotenv import load_dotenv
import os

# loading environment variables
load_dotenv()

# retrieving variables from environment
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
MPESA_PASSKEY = os.getenv('MPESA_PASSKEY')
MPESA_BASE_URL = os.getenv('MPESA_BASE_URL')
MPESA_SHORTCODE = os.getenv('MPESA_SHORTCODE')
CALLBACK_URL = os.getenv('CALLBACK_URL')

# Create your views here.
def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['phone_number']
            amount = form.cleaned_data['amount']

            

    else:
        # display the form
        form = PaymentForm()
        context = {'form': form}
    return render(request, 'camp2025/index.html', context)