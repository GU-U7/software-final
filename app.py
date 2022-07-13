from flask import Flask, request
import psycopg2
import procesos

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="trucos",
    user="postgres",
    password="icg28122002"
)


@app.post("/message")
def message_post():
    datos = request.get_json()
    cur = conn.cursor()



app.run(port=8080, debug=True)