import requests

from proxy.proxy import get_proxy

def scrap_dolar(url):
    # Dirección del servidor proxy al azar en la lista
    proxy = get_proxy()

    # Dirección de la URL a la que quieres acceder
    url = url

    # Realiza la petición GET a través del proxy
    try:
        response = requests.get(url, proxies={"http": proxy, "https": proxy}, verify=True, timeout=30)
    except:
        response = False

    if response:
        if not response.status_code == 200:
            print('STATUS CODE: ', response.status_code)
            print(proxy)
            return False

        # Muestra el contenido de la respuesta si el status code es "200"
        if response.status_code == 200:
            print('STATUS CODE: ', response.status_code)
            # print(proxy)
            print(response.status_code)
            print(url)
            return response.content

    else:
        print('TIME OUT',)
        print('PROXY', proxy)
        print('URL', url)

        return False