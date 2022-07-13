import procesos

def select_topic(conn, topic):
    cur = conn.cursor()
    cur.execute(procesos.buscar(topic))
    filas = cur.fetchall()
    cur.close()
    return str(filas)