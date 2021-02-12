from flask import Flask,request
import pandas as pd
import json
import sqlite3

app = Flask(__name__)

@app.route('/hello/')
def hello():
    return "Hello World!"
print("40")

@app.route('/computemean/',methods=["POST"])
def bye():
    data = request.json
    data = pd.read_json(data,orient="index")
    return data.mean().to_json()

@app.route('/shop/add/',methods=["POST"])
def add_shop():
    data = json.loads(request.json)

    negozio = (data["name"],data["address"],data["products"])
    # Connection to database
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS stores
             (name text, address text, products text)''')
    # Insert a row of data
    c.execute("INSERT INTO stores VALUES (?,?,?)",negozio)

    # Save (commit) the changes
    conn.commit()
    #{"name": "n", "address": "a", "products": "p"}
    conn.close()
    return "Nuovo negozio = " + data["name"] + ", " + data["address"] + ", " + data["products"]

if __name__ == '__main__':
    app.run(debug = True)