from flask import Flask, jsonify, request
import psycopg2
import procesos
import os
from dotenv import load_dotenv
import post_action
import get_action

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
        post_action.insert_into_success(cur, conn, datos)
        return jsonify({'status':'ok'})
    except:
        post_action.insert_into_fail(cur, conn)
        return jsonify({'status':'fail'})
    
@app.get("/message/<topic>")
def message_get(topic):
    return get_action.select_topic(conn, topic)


app.run(port=8080, debug=True)