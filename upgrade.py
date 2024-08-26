from decouple import config
import psycopg2

def actualizar_cotizaciones(data):
    # Conectar a la base de datos
    conn = psycopg2.connect(
        database=config('DATABASE_NAME'),
        user=config('DATABASE_USER'),
        password=config('DATABASE_PASSWORD'),
        host=config('DATABASE_HOST'),
        port=config('DATABASE_PORT')
    )
    cursor = conn.cursor()

    for model, cotizacion in data.items():
        fecha = cotizacion['fechaActualizacion'].split('T')[0]  # Extraer solo la fecha
        
        # Verificar si existe el registro
        cursor.execute(f'SELECT anterior FROM "{model}" WHERE fecha = %s', (fecha,))
        registro = cursor.fetchone()

        print('REGISTRO:', registro)

        if registro:
            anterior = registro[0]  # El valor de 'venta' en la tupla es el primer elemento
            nuevo_venta = cotizacion['venta']
            
            # Determinar nuevos valores para maximo y minimo
            maximo = max(anterior, nuevo_venta)
            minimo = min(anterior, nuevo_venta)
            cierre = nuevo_venta  # siempre se guarda en cierre

            # Actualizar el registro con los valores determinados
            cursor.execute(f"""
                UPDATE "{model}"
                SET maximo = %s, minimo = %s, cierre = %s, compra = %s, anterior = %s
                WHERE fecha = %s
            """, (
                maximo, minimo, cierre,
                cotizacion['compra'], cierre, fecha
            ))
        else:
            # Insertar un nuevo registro
            cursor.execute(f"""
                INSERT INTO "{model}" (fecha, apertura, maximo, minimo, cierre, compra, anterior)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                fecha, cotizacion['venta'], cotizacion['venta'], cotizacion['venta'],
                cotizacion['venta'], cotizacion['compra'], cotizacion['venta']
            ))

    conn.commit()
    cursor.close()
    conn.close()