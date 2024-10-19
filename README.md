# Auto-Loan-Calculator

This Auto Loan Calculator is a web application that allows any user to calculate the monthly payments of a financed car based on down payment value, interest rate, and loan period. This application should provide a devaluation profile of a limited selection of cars, so that the user can decide if it is financially worth to purchase a car based on objective data. 

## Features
- Monthly Payment Calculation: Users can input parameters such as car price, loan duration (in months), interest rate, down payment, and loan start date. The app calculates the monthly payment based on these inputs.
- Interest and Principal Breakdown: A doughnut chart visualizes the ratio between the car price paid and the total interest paid over the loan period.
- Principal Decay Visualization: The decay of the principal is visualized through:
  - Scatter Plot: Displays the principal amount remaining over the course of the loan.
  - Tabular Data: Shows a month-by-month breakdown of the principal remaining.
- Data Persistence: Stores loan calculation outputs in a PostgreSQL database, allowing users to save and revisit past calculations.

## Usage
#### 1. Input the following details in the form:
- Car Price: The total price of the car.
- Loan Duration (Months): The number of months you plan to repay the loan.
- Interest Rate: The annual interest rate (in percentage).
- Down Payment: The amount you will pay upfront.
- Loan Start Date: The date when the loan payments will begin.

#### 2. After submitting, the app will display:
- Monthly Payment: The calculated monthly payment based on the inputs.
- Doughnut Chart: Visualizes the ratio of the car price paid to the total interest paid over the loan.
- Scatter Plot: Shows how the principal decreases over time.
- Table: Lists a month-by-month breakdown of the remaining principal.

## Technology Used

- Backend: Django (Python)
- Database: PostgreSQL
- Frontend: HTML, CSS, JavaScript
- Charts and Visualization: Chart.js for doughnut and scatter plots

## Future Improvements
- Add a user authentication system to allow users to track their loan calculations across sessions.
- Allow the user to select saved loans and compare them on a different UI fragment
- Finalize early payment and refinancing features