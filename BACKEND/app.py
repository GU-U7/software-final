from flask import Flask, jsonify, request
import psycopg2
import procesos
import os
from dotenv import load_dotenv
from flask_wtf import CSRFProtect

load_dotenv()

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

conn = psycopg2.connect(
    host="localhost",
    database="soft_final",
    user="Grove",
    password=os.getenv('db_password')
)


@app.post("/message")
@csrf.exempt
def message_post():
    datos = request.get_json()
    cur = conn.cursor()
    try:
        cur.execute(procesos.insertar(datos["message"], datos["topic"]))
        conn.commit()
        cur.close()
        return jsonify({'status':'ok'})
    except:
        conn.rollback()
        cur.close()
        return jsonify({'status':'fail'})
    
@app.get("/message/<topic>")
@csrf.exempt
def message_get(topic):
    cur = conn.cursor()
    cur.execute(procesos.buscar(topic))
    filas = cur.fetchall()
    cur.close()
    return str(filas)


app.run(port=8080, debug=True)