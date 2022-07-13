from flask import jsonify
import procesos

def insert_into_success(cur, conn, datos):
    cur.execute(procesos.insertar(datos["message"], datos["topic"]))
    conn.commit()
    cur.close()

def insert_into_fail(cur, conn):
    conn.rollback()
    cur.close()