from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.say_hello),
    path("", views.calculate_loan, name="calculate_loan")
]
