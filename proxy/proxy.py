import os
from pathlib import Path
import requests
import json
import csv
import random

# csv dir
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_ROOT = str(os.path.join(BASE_DIR))

def new_proxy():
    # Lista de proxys
    proxy_list = []

    # proxys url
    url = 'https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=responseTime&sort_type=asc&protocols=https'
    url2 = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all'

    # Realiza la petición GET para obtener lista de proxys
    try:
        response = requests.get(url, timeout=30)

    except:
        response = False

    # if response code is 200 ok
    if response and response.status_code == 200:
        # load json
        proxys = json.loads(response.text)
        
        for proxy in proxys['data']:
            proxy_list.append([proxy['ip'] + ':' + proxy['port']])

    if not response or response.status_code != 200:
        # Realiza la petición GET para obtener lista de proxys
        try:
            response = requests.get(url2, timeout=30)

        except:
            response = False

        proxys = response.text.split()
        
        for proxy in proxys:
            proxy_list.append([proxy])

    # create open or create csv
    with open(CSV_ROOT + '/proxy/proxy_list.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(proxy_list)
        
        file.close()

def get_proxy():
    # Lista de proxys
    proxy_list = []

    # open csv
    with open(CSV_ROOT + '/proxy/proxy_list.csv', 'r') as file:
        csvreader = csv.reader(file, delimiter=';')
        for row in csvreader:
            proxy_list.append(row[0])

        file.close()

    # random number fot the list
    n_random = random.randint(0, len(proxy_list) - 1)
    print('NUMERO RANDOM',n_random)
    # get random proxy
    proxy = proxy_list[n_random]

    return proxy

new_proxy()