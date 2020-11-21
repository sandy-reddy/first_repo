import sqlite3

def customerData():
    conn = sqlite3.connect("customer_DB.db")
    cur = conn.cursor()
    cur.execute ("CREATE TABLE IF NOT EXISTS customer (id INTEGER PRIMARY KEY, custID text, firstName text, lastName text, dofB text)")
    conn.commit()
    conn.close()


def addCustRec(custID, firstName, lastName, dofB ):
    conn = sqlite3.connect("customer_DB.db")
    cur = conn.cursor()
    cur.execute ("INSERT INTO customer VALUES (NULL, ?, ?, ?, ?)", (custID, firstName, lastName, dofB))
    conn.commit()
    conn.close()

def viewData():
    conn = sqlite3.connect("customer_DB.db")
    cur = conn.cursor()
    cur.execute ("SELECT * FROM customer")
    rows = cur.fetchall()
    conn.close()
    return rows

def deleteRec(id):
    conn = sqlite3.connect("customer_DB.db")
    cur = conn.cursor()
    cur.execute ("DELETE FROM customer WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def searchData(custID = "", firstName = "", lastName = "", dofB = ""):
    conn = sqlite3.connect("customer_DB.db")
    cur = conn.cursor()
    cur.execute ("SELECT * FROM customer WHERE custID = ? OR firstNAME = ? OR lastName= ? OR dofB = ?", (custID, firstName, lastName, dofB))
    rows = cur.fetchall()
    conn.close()
    return rows

def updateData(id, custID = "", firstName = "", lastName = "", dofB = ""):
    conn = sqlite3.connect("customer_DB.db")
    cur = conn.cursor()
    cur.execute ("UPDATE customer SET custID = ?, firstNAME = ?, lastName= ?, dofB = ?, WHERE id = ?", (custID, firstName, lastName, dofB))
    conn.commit()
    conn.close()
    
customerData()

