
#sqlite3
#psycopg2

# 1 Connect to a database
# 2 Create a cursor object
# 3 Write a SQL query
# 4 Commit changes
# 5 Close connection

import sqlite3


def create_table():

	con = sqlite3.connect("lite.db")
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS games (item TEXT, quantity INTEGER, price REAL)") #create table with columns
	con.commit()
	con.close()
	
def insert(item, qty, price):
	con = sqlite3.connect("lite.db")
	cur = con.cursor()
	#cur.execute("INSERT INTO games VALUES ('Madden', 2, 1.25)")	
	cur.execute("INSERT INTO games VALUES (?,?,?)", (item, qty, price))	
	con.commit()
	con.close()
	

#insert("text",2,2)


def view():
	con = sqlite3.connect("lite.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM games")
	rows=cur.fetchall()	
#	con.commit()  Not needed when fetching data
	con.close()
	return rows

def delete(item):
	con = sqlite3.connect("lite.db")
	cur = con.cursor()
	cur.execute("DELETE FROM games WHERE item=?",(item,))
	con.commit()
	con.close()



def update(price, qty, item):
	con = sqlite3.connect("lite.db")
	cur = con.cursor()
	cur.execute("UPDATE games SET price=?, quantity=? WHERE item=?",(price,qty,item))
	con.commit()
	con.close()



update(3,99999999999,"tacobell")


#delete("22222")
print(view())







