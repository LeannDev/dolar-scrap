import requests
import json

def get_exchanges():

    # Create the API URL for the exchanges
    url = 'https://criptoya.com/api/bancostodos'
    
    # Send a GET request to the API and get the response
    response = requests.get(url)
    
    # Check if the response was successful (status code 200)
    if response.status_code == 200:
        # Load the response data into a Python dictionary
        data = json.loads(response.content.decode('utf-8'))

    else:
        # Do nothing if the response was not successful
        return None

    return data