import requests
import json

# cripto dolar coins
coins = [
    'DAI',
    'USDT',
    'USDC',
    'BUSD',
]

fiats = [
    'ARS',
]

def get_cripto_dolar():
    # Cripto dolar list
    cripto_compra = []
    cripto_venta = []

    # Loop through each coin in the coins list
    for coin in coins:
        # Create the API URL for the coin
        url = f'https://criptoya.com/api/{coin}/ARS/0.1'
        
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
                cripto_compra.append(total_ask)
                cripto_venta.append(total_bid)

        else:
            # Do nothing if the response was not successful
            return None

    # calculate media to dolar cripto
    compra = sum(cripto_compra) / len(cripto_compra)
    venta = sum(cripto_venta) / len(cripto_venta)

    data = {
        'compra': compra,
        'venta': venta,
    }

    return data