from datetime import datetime, time
from time import sleep
import pytz

from url import urls, models
from scrap import scrap_url
from normalize import normalize_data, compare_new_old_data
from db.models import search_model, new_model, update_model
from cripto_dolar.scrap import get_cripto_dolar
from db.cripto_model import search_cripto_model, new_cripto_model, update_cripto_model
from cripto_currency.currency import currencys, fiats, dbs
from cripto_currency.scap import get_cripto
from db.currency_model import search_currency_model, update_currency_model, new_currency_model

# Define the URL to scrape

# Define the timezone
timezone = pytz.timezone("America/Argentina/Buenos_Aires")

# Define the start and end times
start_time = time(11, 0)  # 11:00 AM 
end_time = time(19, 0)  # 7:00 PM

# Define the days of the week to run the scraper
valid_days = [0, 1, 2, 3, 4]  # Monday through Friday

while True:

    # Get the current time in the correct timezone
    now = datetime.now(timezone)
    now_time = now.time()
    
    # Check if it's a valid day and time to run the scraper
    if now.weekday() in valid_days and start_time <= now_time <= end_time:

        # # Run the scraper function
        for url, model in zip(urls, models):

            data = scrap_url(url)

            if data:

                data['db'] = model
                normalized_data = normalize_data(data)

                # search in db
                search_data_db = search_model(normalized_data)

                if search_data_db:
                    # compare price old and new price
                    compare = compare_new_old_data(normalized_data, search_data_db)
                    # update data
                    update = update_model(compare)
                    print('UPDATE DATA IN DB', update)

                else:
                    new_data_db = new_model(normalized_data)
                    print('NEW DATA IN DB', new_data_db)

    # Cripto dolar scrap
    cripto_dolar = get_cripto_dolar()

    if cripto_dolar:
        # search model in db
        search_cripto_db = search_cripto_model(data='scrap_dolarcriptomodel')
        print(search_cripto_db)

        if search_cripto_db:
            # update dolar cripto
            cripto_update = update_cripto_model(cripto_dolar)
            print(cripto_update)

        else:
            # new dolar cripto model
            new_cripto = new_cripto_model(cripto_dolar)
            print(new_cripto)

    # Cripto currency scrap
    for currency, db in zip(currencys, dbs):
    
        # Determine fiat currency based on the current currency
        if currency == 'DAI' or currency == 'USDT' or currency == 'USDC' or currency == 'DOGE':
            fiat = fiats[1]
        else:
            fiat = fiats[0]

        # Create a data object with currency, fiat, and database info
        data = {
            'currency': currency,
            'fiat': fiat,
            'db': db,
        }

        # Call get_cripto function with the data object to retrieve current currency information
        get_currency = get_cripto(data)

        data['compra'] = get_currency['compra']

        if get_currency:
            # Search for currency in the database
            search_currency = search_currency_model(data)

            if search_currency:
                # Update currency in the database
                update = update_currency_model(data)

            else:
                # Insert new currency into the database
                new = new_currency_model(data)

    
    # Wait for 30 minutes before running again
    sleep(1800)  # 30 minutes in seconds