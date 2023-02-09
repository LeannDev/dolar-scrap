from datetime import datetime
from time import sleep
import pytz

from launch import launch
from proxy.proxy import new_proxy

# get proxys for first time
new_proxy()

# fecha actual
now = datetime.now(pytz.timezone('America/Argentina/Buenos_Aires'))

# hora
hour = int(now.strftime("%-H"))
# minutes
minutes = int(now.strftime('%M'))
# dia de la semana
weekday = int(now.strftime("%w"))

while True:
    # entre lunes y viernes
    if weekday >= 1 and weekday <= 5:

        # horario de operacion de mercado
        if hour >= 11 and hour <= 17:
            print(now)
            launch()
            sleep(1500)

        if hour == 18 and minutes >= 40:
            launch()
            sleep(1500)

        # else:
            # print('STOCKS CLOSED')

    # else:
        # print('WEEKEND')

    sleep(1)

#test de git