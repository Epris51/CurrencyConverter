import requests

def convert_currency(from_currency, to_currency, amount):
    """
    Convert currency using exchangerate.host API

    Args:
        from_currency (str): Currency code to convert from (e.g., 'USD')
        to_currency (str): Currency code to convert to (e.g., 'EUR')
        amount (float): Amount to convert

    Returns:
        float: Converted amount
    """
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url)
    data = response.json()
    converted_amount = data["result"]
    return converted_amount
