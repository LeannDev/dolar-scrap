import json
from datetime import datetime, date

from url import urls, models
from get_content import scrap_dolar
from db.models import search_model, new_model, update_model
from proxy.proxy import new_proxy

def launch():
    i = 0
    attemps = 15

    # bucle while para recorrer la lista de url
    while i <= 4 and i >= 0:

        # realizar scrap y guardar en variable
        data = scrap_dolar(urls[i])

        # si devuelve la data
        if data:

            data = json.loads(data)
            
            # format date
            date = datetime.strptime(data['fecha'].replace('/','-'), "%d-%m-%Y - %H:%M")

            # /////////// CREAR FORMA DE DETECTAR SI EXISTE DATA DE ESE DIA y ACTUALIZAR O CREAR NUEVA SEGUN CORRESPONDA //////////////
            scrap_data = {
                'db': models[i],
                'date': date.date(),
                'buy': float(data['compra'].replace(',','.')),
                'sale': float(data['venta'].replace(',','.')),
            }

            # search in db
            search_db = search_model(scrap_data)

            if search_db:
                # update data
                print('DATA TRUE')

                scrap_data['id'] = search_db[0]
                scrap_data['previous'] = scrap_data['sale']

                if scrap_data['sale'] > search_db[3]:
                    scrap_data['max'] = scrap_data['sale']

                else:
                    scrap_data['max'] = search_db[3]

                if scrap_data['sale'] < search_db[4]:
                    scrap_data['min'] = scrap_data['sale']

                else:
                    scrap_data['min'] = search_db[4]

                update_data = update_model(scrap_data)
                print('UPDATE DATA', update_data)

            else:
                new_data = new_model(scrap_data)
                print('NEW DATA IN DB', new_data)

            print('SCRAP DATA',scrap_data)
            i += 1
            attemps = 15


        # si no devuelve la data resta 1 para repetir con otro proxy
        if not data:
            print('NOT DATA', data)
            
            attemps -= 1

        # si se agotan los intentos termina el bucle
        if attemps <= 0:
            new_proxy()
            attemps = 15
            # break

        print('I', i)
        print('ATTEMPS', attemps)