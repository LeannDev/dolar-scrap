from db.connect import con

# search model
def search_currency_model(data):
    cur = con.cursor()
    
    try:
        query = """
        SELECT * FROM {} WHERE id = %s
        """.format(data['db'])
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
def new_currency_model(data):
    cur = con.cursor()

    try:
        if data['currency'] == 'DAI' or data['currency'] == 'USDT' or data['currency'] == 'USDC':
            query = """
                INSERT INTO {table} 
                (venta, id)
                VALUES (%s, %s)
            """

            cur.execute(
                query.format(table=data['db']),(data['compra'], 1)
            )

        else:
            query = """
                INSERT INTO {table} 
                (precio, symbol, id)
                VALUES (%s, %s, %s)
            """

            cur.execute(
                query.format(table=data['db']),(data['compra'], data['currency'], 1)
            ) 

    except:
       con.rollback()

    con.commit()
    cur.close()

    return cur.rowcount

# update
def update_currency_model(data):
    cur = con.cursor()

    try:
        if data['currency'] == 'DAI' or data['currency'] == 'USDT' or data['currency'] == 'USDC':
            query = """
        UPDATE {table} 
        SET venta = %s
        WHERE id = %s
        """
            cur.execute(
                query.format(table=data['db']),(data['compra'], 1)
            )
            
        else:
            query = """
            UPDATE {table} 
            SET precio = %s, symbol = %s
            WHERE id = %s
            """

            cur.execute(
                query.format(table=data['db']),(data['compra'], data['currency'], 1)
            )

    except:
       con.rollback()

    con.commit()
    cur.close()

    return cur.rowcount