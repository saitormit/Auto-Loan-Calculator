import json

from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect, get_object_or_404
from .forms import LoanForm
from datetime import datetime
from dateutil.relativedelta import relativedelta

from .models import LoanDetails


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


def arrange_display_data(principal, loan_duration, interest, monthly_payment, start_date):
    plot_data, table_data = [], []
    interest_pay, principal_pay = 0, 0
    curr_date = start_date
    for month in range(loan_duration+1):
        plot_data.append({'x': month, 'y': round(principal, 2)})
        table_data.append({'Month': month,
                           'Payment date': curr_date.strftime('%m/%d/%Y'),
                           'Principal portion': round(principal_pay, 2),
                           'Interest portion': round(interest_pay, 2),
                           'Remaining balance': round(principal, 2)})
        interest_pay = (interest/12/100) * principal
        principal_pay = monthly_payment - interest_pay
        principal -= principal_pay
        curr_date = curr_date + relativedelta(months=1)

    return json.dumps(plot_data), json.dumps(table_data)


def calculate_loan(request):

    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            car_price = form.cleaned_data['car_price']
            loan_duration = form.cleaned_data['loan_duration']
            interest = form.cleaned_data['interest']
            down_payment = form.cleaned_data['down_payment']
            start_date = form.cleaned_data['start_date']
            refi_start_date = form.cleaned_data['refi_start_date']
            refi_interest = form.cleaned_data.get('refi_interest')
            refi_loan_duration = form.cleaned_data.get('refi_loan_duration')

            monthly_payment = calculate_monthly_payment(car_price, loan_duration, interest, down_payment)
            loaned_amount = car_price - down_payment
            total_interest_amount = monthly_payment * loan_duration - loaned_amount
            total_price_amount = car_price + total_interest_amount
            plot_data, table_data = arrange_display_data(car_price - down_payment, loan_duration, interest, monthly_payment, start_date)

            # Saved data in database
            loan_details = LoanDetails(
                car_price = car_price,
                loan_duration=loan_duration,
                start_date=start_date,
                interest=interest,
                down_payment=down_payment,
                monthly_payment=monthly_payment
            )
            loan_details.save()

        else:
            print(form.errors)
            car_price = loan_duration = interest = down_payment = start_date = refi_interest = refi_loan_duration = refi_start_date = None
            monthly_payment = loaned_amount = total_interest_amount = total_price_amount = plot_data = table_data = None
    else:
        form = LoanForm()
        # Default values
        car_price = 25000
        loan_duration = 48
        interest = 4.50
        down_payment = 5000
        start_date = datetime.today()
        refi_start_date = None
        refi_interest = None
        refi_loan_duration = None
        monthly_payment = calculate_monthly_payment(car_price, loan_duration, interest, down_payment)
        loaned_amount = car_price - down_payment
        total_interest_amount = monthly_payment * loan_duration - loaned_amount
        total_price_amount = car_price + total_interest_amount
        plot_data, table_data = arrange_display_data(car_price - down_payment, loan_duration, interest, monthly_payment, start_date)

    loan_calculation = LoanDetails.objects.all()

    return render(request, 'calculator/main.html',
                  {'form': form,
                   'car_price': car_price,
                   'loan_duration': loan_duration,
                   'interest': interest,
                   'start_date': start_date,
                   'monthly_payment': monthly_payment,
                   'down_payment': down_payment,
                   'loaned_amount': loaned_amount,
                   'refi_interest': refi_interest,
                   'refi_loan_duration': refi_loan_duration,
                   'refi_start_date': refi_start_date,
                   'total_interest_amount': total_interest_amount,
                   'total_price_amount': total_price_amount,
                   'plot_data': plot_data,
                   'table_data': table_data,
                   'loan_details': loan_calculation})


def delete_loan(request, loan_id):
    loan = get_object_or_404(LoanDetails, id=loan_id)
    loan.delete()
    return redirect('calculate_loan')