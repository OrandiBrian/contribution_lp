from django.shortcuts import render
from .forms import PaymentForm
from dotenv import load_dotenv
import os, requests, base64, json, re
from datetime import datetime

# loading environment variables
load_dotenv()

# retrieving variables from environment
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
MPESA_PASSKEY = os.getenv('MPESA_PASSKEY')
MPESA_BASE_URL = os.getenv('MPESA_BASE_URL')
MPESA_SHORTCODE = os.getenv('MPESA_SHORTCODE')
CALLBACK_URL = os.getenv('CALLBACK_URL')

# generate access token
def generate_access_token():
    url = f"{MPESA_BASE_URL}/oauth/v1/generate?grant_type=client_credentials"

    try:
        # encodeing credentials
        encoded_credentials = base64.b64encode(f"{CONSUMER_KEY}:{CONSUMER_SECRET}".encode()).decode()

        headers = {'Authorization': f"Basic {encoded_credentials}", 'Content-Type': 'application/json'}

        # sending requests
        response = requests.get(url, headers=headers).json()

        # checking if there are errors
        if "access_token" in response:
            return response['access_token']
        else:
            raise Exception("Access token not found in response")
    except Exception as e:
        raise Exception(f"Error generating access token: {str(e)}")
    
# Function to send STK push
def send_stk_push(phone_number, amount):
    try:
        token = generate_access_token()
        url = f"{MPESA_BASE_URL}/mpesa/stkpush/v1/processrequest"
        headers = {
            'Authorization': f"Bearer {token}",
            'Content-Type': 'application/json'
        }

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        stk_password = base64.b64encode((MPESA_SHORTCODE + MPESA_PASSKEY + timestamp).encode()).decode()

        payload = {
            "BusinessShortCode": "174379",
            "Password": stk_password,
            "Timestamp":timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",
            "PartyA":phone_number,
            "PartyB":"174379",
            "PhoneNumber":phone_number,
            "CallBackURL": CALLBACK_URL,
            "AccountReference":"EdenSprings",
            "TransactionDesc":"Camp2025"
        }

        # sending the requests
        response = requests.post(url, headers=headers, json=payload).json()

        return response
    
    except Exception as e:
        raise Exception(f"Error sending STK push: {str(e)}")
    
# phone number formating function
def format_phone_number(phone_number):
    phone = phone_number.replace("+", "")
    if re.match(r"^254\d{9}$", phone):
        return phone
    elif phone.startswith("0") and len(phone) == 10:
        return "254" + phone[1:]
    else:
        raise ValueError("Invalid Phone Number Format. Start with 254...")

# Create your views here.
def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            phone = format_phone_number(form.cleaned_data['phone_number'])
            amount = int(form.cleaned_data['amount'])
            
            response = send_stk_push(phone, amount)

            if response.get('ResponseCode') == '0':
                print(response)
                return render(request, 'camp2025/pending.html')
            else:
                errorMessage =response.get('errorMessage', 'Failed to initiate payment. Please try again')
                context = {'form': form, 'errorMessage': errorMessage}
                return render(request, 'camp2025/index.html', context)

    else:
        # display the form
        form = PaymentForm()
        context = {'form': form}
    return render(request, 'camp2025/index.html', context)