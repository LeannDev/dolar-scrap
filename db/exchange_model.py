from db.connect import con

# search model
def search_exchange_model(data):
    cur = con.cursor()
    
    try:
        query = """
        SELECT * FROM {} WHERE LOWER(nombre) = LOWER(%s)
        """.format(data['db'])
        cur.execute(query, (data['nombre'],))

        data = cur.fetchone()

    except Exception as e:
        print(f"Error: {e}")
        data = None
        con.rollback()

    con.commit()
    cur.close()

    return data

# register new data in db
def new_exchange_model(data):
    cur = con.cursor()

    try:
        query = """
            INSERT INTO {table} 
            (nombre, compra, venta, solidario, slug, online)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        cur.execute(
            query.format(table=data['db']),(data['nombre'].capitalize(), data['compra'], data['venta'], data['solidario'], data['nombre'].lower(), False)
        ) 

    except:
       con.rollback()

    con.commit()
    cur.close()

    return cur.rowcount

# update
def update_exchange_model(data):
    cur = con.cursor()

    try:
        query = """
        UPDATE {table} 
        SET compra = %s, venta = %s, solidario = %s
        WHERE LOWER(nombre) = LOWER(%s)
        """

        cur.execute(
            query.format(table=data['db']),(data['compra'], data['venta'], data['solidario'], data['nombre'])
        )

    except:
       con.rollback()

    con.commit()
    cur.close()

    return cur.rowcount