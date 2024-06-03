from django import forms


class LoanForm(forms.Form):
    car_price = forms.IntegerField(label="Car price ($)")
    loan_duration = forms.IntegerField(label="Loan duration (months)")
    interest = forms.FloatField(label="Interest rate (%)")
    down_payment = forms.IntegerField(label="Down payment ($)")
