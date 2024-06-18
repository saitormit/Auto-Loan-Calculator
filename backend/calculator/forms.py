from django import forms


class LoanForm(forms.Form):
    car_price = forms.IntegerField(label="Car price ($)")
    loan_duration = forms.IntegerField(label="Loan duration (months)")
    interest = forms.FloatField(label="Interest rate (%)")
    down_payment = forms.IntegerField(label="Down payment ($)")
    start_date = forms.DateField(input_formats=['%m/%d/%Y'],
                                 widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}))
    refi_interest = forms.FloatField(label="New interest rate (%)", required=False)
    refi_loan_duration = forms.IntegerField(label="New loan duration (months)", required=False)
    refi_start_date = forms.DateField(input_formats=['%m/%d/%Y'],
                                 widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}), required=False)
