from django.shortcuts import render
from .forms import PaymentForm

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