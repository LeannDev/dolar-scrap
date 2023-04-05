import requests
import json

def get_cripto(data):
    # Cripto dolar list
    currency_buy = []
    currency_sell = []
    
    # Create the API URL for the currency
    url = f'https://criptoya.com/api/{data["currency"]}/{data["fiat"]}/0.1'
    
    # Send a GET request to the API and get the response
    response = requests.get(url)
    
    # Check if the response was successful (status code 200)
    if response.status_code == 200:
        # Load the response data into a Python dictionary
        data = json.loads(response.content.decode('utf-8'))

        # Loop through each exchange in the data dictionary
        for exchange in data:
            # Get the totalAsk value for the current exchange
            total_ask = data[exchange]['totalAsk']
            total_bid = data[exchange]['totalBid']

            # append results in cripto list
            currency_buy.append(total_ask)
            currency_sell.append(total_bid)

    else:
        # Do nothing if the response was not successful
        return None

    # calculate media to dolar cripto
    compra = sum(currency_buy) / len(currency_buy)
    venta = sum(currency_sell) / len(currency_sell)

    data = {
        'compra': compra,
        'venta': venta,
    }

    # Convert data to JSON
    json_data = json.dumps(data)

    return data