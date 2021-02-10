import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS stores
             (name text, address text, products text)''')

# Insert a row of data
c.execute("INSERT INTO stores VALUES ('test shop','via test, bergamo','[\"frutta\", \"verdura\"]')")

# Save (commit) the changes
conn.commit()


# Do this instead
t = ('test shop',)
c.execute('SELECT * FROM stores WHERE name=?', t)
print(c.fetchone())

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

