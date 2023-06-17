from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Fetch currency symbols from API
    url = 'https://api.exchangerate.host/symbols'
    response = requests.get(url)
    data = response.json()

    # Extract currency codes and country names
    currencies = [{'code': code, 'name': data['symbols'][code]['description']} for code in data['symbols']]

    return render_template('form.html', currencies=currencies)

@app.route('/convert', methods=['POST'])
def convert():
    currency_from = request.form.get('currency_from')
    currency_to = request.form.get('currency_to')
    amount = request.form.get('amount')

    # Validate form data
    if not currency_from or not currency_to or not amount:
        error = 'Please fill in all fields.'
        currencies = get_currencies()
        return render_template('form.html', error=error, currencies=currencies)

    try:
        amount = float(amount)
    except ValueError:
        error = 'Invalid amount. Please enter a valid number.'
        currencies = get_currencies()
        return render_template('form.html', error=error, currencies=currencies)

    # Make API call to exchangerate.host
    url = f'https://api.exchangerate.host/convert?from={currency_from}&to={currency_to}&amount={amount}'
    response = requests.get(url)
    data = response.json()

    if 'result' in data:
        result = data['result']
        return render_template('results.html', amount=amount, currency_from=currency_from, currency_to=currency_to, result=result)
    elif 'error' in data:
        error = data['error']
        currencies = get_currencies()
        return render_template('form.html', error=error, currencies=currencies)
    else:
        error = 'Failed to retrieve exchange rate. Please try again.'
        currencies = get_currencies()
        return render_template('form.html', error=error, currencies=currencies)

def get_currencies():
    # Fetch currency symbols from API
    url = 'https://api.exchangerate.host/symbols'
    response = requests.get(url)
    data = response.json()

    # Extract currency codes and country names
    currencies = [{'code': code, 'name': data['symbols'][code]['description']} for code in data['symbols']]

    return currencies

if __name__ == '__main__':
    app.run(debug=True)



