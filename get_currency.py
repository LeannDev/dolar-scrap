import requests

def get_dollar_quotes():
    """Fetches the dollar exchange rates from the dolarapi.com API.

    Returns:
        dict: A dictionary containing the dollar exchange rates if the request is successful,
              or None if an error occurs.
    """

    url = "https://dolarapi.com/v1/dolares"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for error HTTP status codes

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching quotes: {e}")
        return None