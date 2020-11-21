import sqlite3
from customer import Customer

conn = sqlite3.connect("customer.db")

c = conn.cursor()

# c.execute("""CREATE TABLE customers (
#             first text,
#             last text,
#             dofb text,
#             custid integer
#             )""")

# cust_1 = Customer ("Sam", "Bob", "1-1-1990", 1)
# cust_2 = Customer ("Joe", "Bob", "1-1-1990", 2)


# c.execute("INSERT INTO customers VALUES (?, ?, ?, ?)", (cust_1.first, cust_1.last, cust_1.dofb, cust_1.custid))

# c.execute("INSERT INTO customers VALUES ('Sandeep', 'Siddapureddy', '1-23-1997', 000000)")

c.execute ("SELECT * FROM customers WHERE last=?", ("Bob"))

print(c.fetchall())

conn.commit()

conn.close()



