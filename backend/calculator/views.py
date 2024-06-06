import json

from django.shortcuts import render, HttpResponse
from .forms import LoanForm


# Create your views here.
def say_hello(request):
    return HttpResponse("Hello world")


def calculate_monthly_payment(car_price, loan_duration, interest, down_payment):
    principal = car_price - down_payment
    # Monthly interest rate
    r = interest / 12 / 100
    # Number of months for the loan
    if r == 0:
        return principal / loan_duration
    return principal * (r * (1 + r)**loan_duration) / ((1 + r)**loan_duration - 1)


def arrange_plot_data(principal, loan_duration, interest, monthly_payment):
    plot_data, table_data = [], []
    interest_pay, principal_pay = 0, 0
    for month in range(loan_duration+1):
        plot_data.append({'x': month, 'y': round(principal, 2)})
        table_data.append({'Month': month,
                           'Principal portion': round(principal_pay, 2),
                           'Interest portion': round(interest_pay, 2),
                           'Remaining balance': round(principal, 2)})
        interest_pay = (interest/12/100) * principal
        principal_pay = monthly_payment - interest_pay
        principal -= principal_pay

    return json.dumps(plot_data), json.dumps(table_data)


def calculate_loan(request):
    # Default values
    car_price = 25000
    loan_duration = 48
    interest = 4.5
    down_payment = 5000
    monthly_payment = calculate_monthly_payment(car_price, loan_duration, interest, down_payment)
    loaned_amount = car_price - down_payment
    total_interest_amount = monthly_payment * loan_duration - loaned_amount
    total_price_amount = car_price + total_interest_amount
    plot_data, table_data = arrange_plot_data(car_price-down_payment, loan_duration, interest, monthly_payment)

    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            car_price = form.cleaned_data['car_price']
            loan_duration = form.cleaned_data['loan_duration']
            interest = form.cleaned_data['interest']
            down_payment = form.cleaned_data['down_payment']
            monthly_payment = calculate_monthly_payment(car_price, loan_duration, interest, down_payment)
            loaned_amount = car_price - down_payment
            total_interest_amount = monthly_payment * loan_duration - loaned_amount
            total_price_amount = car_price + total_interest_amount
            plot_data, table_data = arrange_plot_data(car_price - down_payment, loan_duration, interest, monthly_payment)

        else:
            print(form.errors)
    else:
        form = LoanForm()

    return render(request, 'calculator/main.html',
                  {'form': form,
                   'car_price': car_price,
                   'loan_duration': loan_duration,
                   'interest': interest,
                   'monthly_payment': monthly_payment,
                   'down_payment': down_payment,
                   'loaned_amount': loaned_amount,
                   'total_interest_amount': total_interest_amount,
                   'total_price_amount': total_price_amount,
                   'plot_data': plot_data,
                   'table_data': table_data})
