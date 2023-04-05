from db.connect import con

# search model
def search_cripto_model(data):
    cur = con.cursor()
    
    try:
        query = """
        SELECT * FROM {} WHERE id = %s
        """.format(data)
        cur.execute(query, (1,))

        data = cur.fetchone()

    except Exception as e:
        print(f"Error: {e}")
        data = None
        con.rollback()

    con.commit()
    cur.close()

    return data

# register new data in db
def new_cripto_model(data):
    cur = con.cursor()

    try:
        query = """
            INSERT INTO {table} 
            (compra, venta, id)
            VALUES (%s, %s, %s)
        """

        table_name = 'scrap_dolarcriptomodel'

        cur.execute(
            query.format(table=table_name),(data['venta'], data['compra'], 1)
        ) 

    except:
       con.rollback()

    con.commit()
    cur.close()

    return cur.rowcount

# update
def update_cripto_model(data):
    cur = con.cursor()

    try:
        query = """
        UPDATE {table} 
        SET compra = %s, venta = %s
        WHERE id = %s
        """
        table_name = 'scrap_dolarcriptomodel'

        cur.execute(
            query.format(table=table_name),(data['venta'], data['compra'], 1)
        )

    except:
       con.rollback()

    con.commit()
    cur.close()

    return cur.rowcount
