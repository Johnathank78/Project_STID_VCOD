from flask import Flask
import mysql.connector

connection = mysql.connector.connect(
    host = 'db',
    user = 'root',
    passwd = 'root',
    port = '3306',
    database = 'footdirect'
)

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "<p>Hello, World!</p>"