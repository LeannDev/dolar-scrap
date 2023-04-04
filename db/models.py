from db.connect import con

# search model
def search_model(data):
    cur = con.cursor()

    try:
        query = """
        SELECT * FROM {} WHERE fecha = %s
        """.format(data['db'])
        cur.execute(query, (data['fecha'],))

        data = cur.fetchone()

    except Exception as e:
        print(f"Error: {e}")
        data = None
        con.rollback()

    con.commit()
    cur.close()

    return data

# new register new data in db
def new_model(data):
    cur = con.cursor()

    try:
        cur.execute(f"""
        INSERT INTO {data['db']} 
        (fecha, cierre, compra, apertura, maximo, minimo, anterior)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (data['fecha'], data['venta'], data['compra'], data['venta'], data['venta'], data['venta'], data['venta'])) 

    except:
       con.rollback()

    con.commit()
    cur.close()

    return cur.rowcount

# update
def update_model(data):
    cur = con.cursor()

    try:
        query = """
        UPDATE {table} 
        SET maximo = %s, minimo = %s, cierre = %s, compra = %s, anterior = %s
        WHERE id = %s
        """
        table_name = data['db']

        cur.execute(
            query.format(table=table_name),(data['max'], data['min'], data['venta'], data['compra'], data['anterior'], data['id'])
        )

    except:
       con.rollback()

    con.commit()
    cur.close()

    return cur.rowcount
