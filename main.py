from datetime import datetime, time
from time import sleep
import pytz

from url import urls, models
from scrap import scrap_url
from normalize import normalize_data, compare_new_old_data
from db.models import search_model, new_model, update_model
from cripto_dolar.scrap import get_cripto_dolar
from db.cripto_model import search_cripto_model, new_cripto_model, update_cripto_model

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

                
    
    # Wait for 30 minutes before running again
    sleep(1800)  # 30 minutes in seconds