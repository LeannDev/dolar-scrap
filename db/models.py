from db.connect import con

# open cursor
#cur = con.cursor()

# search model
def search_model(data):
    cur = con.cursor()

    try:
        cur.execute(f"""
        SELECT * FROM {data['db']}
        WHERE fecha = %s
        """, (data['date'],)
        )

        data = cur.fetchone()

        print('DATA CUR', data)

    except:
        data = None
        con.rollback()

    con.commit()
    cur.close()
    #con.close()

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
        (data['date'], data['sale'], data['buy'], data['sale'], data['sale'], data['sale'], data['sale'])) # apertura, maximo, minimo, anterior

        data = cur.query
        print(data)

    except:
       data = None
       con.rollback()

    con.commit()
    cur.close()
    # con.close()

    return data

# update
def update_model(data):
    cur = con.cursor()

    try:
        cur.execute(f"""
        UPDATE %s 
        SET maximo = %s, minimo = %s, cierre = %s, compra = %s, anterior = %s
        WHERE id = %s
        """,
        (data['db'], data['max'], data['min'], data['sale'], data['buy'], data['previous'], data['id']))

        data = cur.query
        print(data)

    except:
       data = None
       con.rollback()

    con.commit()
    cur.close()
    # con.close()

    return data
