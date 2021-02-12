import requests
import json
import sqlite3

d = {"name": "luigino", "address": "via ministero", "products": "esteri"}

r = requests.post("http://127.0.0.1:5000/shop/add/",json = json.dumps(d))

#Verifica che il database sia stato popolato
conn = sqlite3.connect('example.db')
c = conn.cursor()
t = ('luigino',)
c.execute('SELECT * FROM stores WHERE name LIKE ?',t)

while True :
    # Do this instead
    a = c.fetchone()
    print(a)
    if a is None :
        break

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()