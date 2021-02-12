import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS stores
             (name text, address text, products text)''')

negozio = ('theonlyone','via nuova','cose a km 0')

# Insert a row of data
c.execute("INSERT INTO stores VALUES (?,?,?)",negozio)
#c.execute("INSERT INTO stores VALUES ('test panettiere','via marconi, bergamo','[\"pane\", \"pasticcini\"]')")
#c.execute("INSERT INTO stores VALUES ('shop','via marconi, bergamo','[\"ricotta\", \"taleggio\"]')")

# Save (commit) the changes
conn.commit()

t = ('theonlyone',)
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

