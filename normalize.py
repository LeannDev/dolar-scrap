
from datetime import datetime

def normalize_data(data):

    # format date
    date = datetime.strptime(data['fecha'].replace('/','-'), "%d-%m-%Y - %H:%M")
    print('FORMAT DATE', date)

    # add taxes in dolar turista
    if data['db'] == 'scrap_dolarturistamodel':

        compra = float(data['compra'].replace(',','.'))+((75/100)*float(data['compra'].replace(',','.')))
        venta = float(data['venta'].replace(',','.'))+((75/100)*float(data['venta'].replace(',','.')))

    else: 

        compra = float(data['compra'].replace(',','.'))
        venta = float(data['venta'].replace(',','.'))

    data['fecha'] = date.date()
    data['compra'] = compra
    data['venta'] = venta

    return data

def compare_new_old_data(data, data_db):

    data['id'] = data_db[0]
    data['anterior'] = data['venta']

    if data['venta'] > data_db[3]:
        data['max'] = data['venta']

    else:
        data['max'] = data_db[3]

    if data['venta'] < data_db[4]:
        data['min'] = data['venta']

    else:
        data['min'] = data_db[4]

    return data
