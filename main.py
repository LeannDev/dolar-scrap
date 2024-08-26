import time
from datetime import datetime

from get_currency import get_dollar_quotes
from mapping import match_models_with_data
from upgrade import actualizar_cotizaciones
from listdb import names_db

def main_loop():
    while True:
        now = datetime.now()
        day_of_week = now.weekday()  # 0: Lunes, 6: Domingo
        current_hour = now.hour

        # Ejecutar solo de lunes a viernes (0-4) y entre 10 a.m. y 4 p.m.
        if 0 <= day_of_week <= 4 and 10 <= current_hour < 16:
            print(f"Ejecutando actualización: {now}")

            json_data = get_dollar_quotes()

            mappings = match_models_with_data(json_data, names_db)
            print(mappings)

            if mappings:
                actualizar_cotizaciones(mappings)
            else:
                print("Failed to fetch quotes.")
        else:
            print(f"Fuera de horario laboral: {now}")

        # Esperar 30 minutos (1800 segundos)
        time.sleep(1800)

if __name__ == "__main__":
    main_loop()