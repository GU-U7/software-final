from flask import Flask, jsonify, request
import psycopg2
import procesos
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="soft_final",
    user="Grove",
    password=os.getenv('db_password')
)


@app.post("/message")
def message_post():
    datos = request.get_json()
    cur = conn.cursor()
    try:
        cur.execute(procesos.insertar(datos["message"], datos["topic"]))
        conn.commit()
        return jsonify({'status':'ok'})
    except:
        conn.rollback()
        return jsonify({'status':'fail'})
    



app.run(port=8080, debug=True)