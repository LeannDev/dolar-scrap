import os
from dotenv import load_dotenv
import requests
import json
import time

# load dotenv
load_dotenv()

def scrap_url(url):
    """
    Scrape the content of a given URL using ScraperAPI's asynchronous API.
    Args:
        url (str): The URL to scrape.
    Returns:
        str: The scraped content if the status code of the response is 200, otherwise returns None.
    """

    # Send a POST request to ScraperAPI to start the scraping job
    response = requests.post(
        url = 'https://async.scraperapi.com/jobs',
        json={
            'apiKey': os.getenv('API_KEY'),
            'url': url
        }
    )

    # Parse the JSON response into a dictionary
    data = json.loads(response.text)

    # Wait for 15 seconds to let the scraping job start
    time.sleep(15)

    # Keep checking the status of the job until it finishes
    while True:

        response = requests.get(
            url = data['statusUrl']
        )

        data = json.loads(response.text)

        if data['status'] == 'finished':

            # If the status code of the response is 200, return the scraped content
            if data['response']['statusCode'] == 200:

                return data['response']['body']
            
            # If the status code is not 200, return None
            else:
                
                return None
            
        else:

            time.sleep(20)

    # This line will never be reached, but it's included for completeness
    return None