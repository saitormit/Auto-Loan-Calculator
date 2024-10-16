from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.say_hello),
    path("", views.calculate_loan, name="calculate_loan"),
    path('delete/<int:loan_id>/', views.delete_loan, name='delete_loan'),  # URL for deleting a loan calculation
]
