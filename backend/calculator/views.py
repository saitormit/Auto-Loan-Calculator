from django.shortcuts import render, HttpResponse
from .forms import LoanForm


# Create your views here.
def say_hello(request):
    return HttpResponse("Hello world")


def home(request):
    return render(request, "calculator/main.html")


def calculate_monthly_payment(car_price, loan_duration, interest, down_payment):
    principal = car_price - down_payment
    # Monthly interest rate
    r = interest / 12 / 100
    # Number of months for the loan
    if r == 0:
        return principal / loan_duration
    return principal * (r * (1 + r)**loan_duration) / ((1 + r)**loan_duration - 1)


def calculate_loan(request):
    monthly_payment = None
    loaned_amount = None
    down_payment = 0
    total_interest_amount = None
    total_price_amount = None

    if request.method == 'POST':
        form = LoanForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            car_price = form.cleaned_data['car_price']
            loan_duration = form.cleaned_data['loan_duration']
            interest = form.cleaned_data['interest']
            down_payment = form.cleaned_data['down_payment']
            monthly_payment = calculate_monthly_payment(car_price, loan_duration, interest, down_payment)
            loaned_amount = car_price - down_payment
            total_interest_amount = loaned_amount * interest * loan_duration/12
            total_price_amount = car_price + total_interest_amount
        else:
            print(form.errors)
    else:
        form = LoanForm()

    return render(request, 'calculator/main.html',
                  {'form': form,
                   'monthly_payment': monthly_payment,
                   'down_payment': down_payment,
                   'loaned_amount': loaned_amount,
                   'total_interest_amount': total_interest_amount,
                   'total_price_amount': total_price_amount})
