import os
import json
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Store expenses and earnings
expenses = []
total_earnings = 1  # Default earning is ₹1

# Route for the home page
@app.route('/')
def index():
    # Calculate total expenditure
    total_expenditure = sum(expense['amount'] for expense in expenses)
    remaining_balance = total_earnings - total_expenditure
    return render_template('index.html', expenses=expenses, total_earnings=total_earnings,
                           total_expenditure=total_expenditure, remaining_balance=remaining_balance)

# Route to add an expense
@app.route('/add', methods=['POST'])
def add_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        category = request.form['category']
        date = datetime.now().strftime('%Y-%m-%d')
        expenses.append({'description': description, 'amount': amount, 'category': category, 'date': date})
        return redirect(url_for('index'))

# Route to add earnings
@app.route('/add_earnings', methods=['POST'])
def add_earnings():
    global total_earnings
    if request.method == 'POST':
        earnings = float(request.form['earnings'])
        total_earnings += earnings  # Add earnings to the total
        return redirect(url_for('index'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
