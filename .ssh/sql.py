import sqlite3
con = sqlite3.connect('personal.sqlite3')

cur = con.cursor()

# Create table
#ur.execute('''CREATE TABLE stocks
               #(date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cur.execute("INSERT INTO personal VALUES (2, 'Ayami','198')")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()