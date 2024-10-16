from django.db import models

# Create your models here.
class LoanDetails(models.Model):
    car_price = models.DecimalField(max_digits=10, decimal_places=2)
    loan_duration = models.IntegerField()  # Duration in months
    interest = models.DecimalField(max_digits=5, decimal_places=2)  # Interest rate percentage
    down_payment = models.DecimalField(max_digits=10, decimal_places=2)  # Down payment amount
    start_date = models.DateField()  # Start date of the loan
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2)  # Monthly payment
    calculated_at = models.DateTimeField(auto_now_add=True)  # Automatically stores timestamp

    def __str__(self):
        return f'Loan for {self.car_price} calculated on {self.calculated_at}'

    def calculate_total_interest(self):
        pass