
#sqlite3
#psycopg2



# 1 Connect to a database
# 2 Create a cursor object
# 3 Write a SQL query
# 4 Commit changes
# 5 Close connection

import sqlite3



def create_table():

	con = sqlite3.connect("gamesData.db")
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS games (item TEXT, upc, console TEXT, price REAL, complete, nib)") #create table with columns
	con.commit()
	con.close()
	
def insert(title, upc, system, value, complete, nib):
	con = sqlite3.connect("gamesData.db")
	cur = con.cursor()
	#cur.execute("INSERT INTO games VALUES ('Madden', 2, 1.25)")	
	cur.execute("INSERT INTO games VALUES (?,?,?,?,?,?)", (title, upc, system, value, complete, nib))	
	con.commit()
	con.close()

create_table()


def addtitle():
	title = input("Title of the Game?: ")
	upc = input("UPC: ")
	system = input("Console?: ")
	value = input("Latest Value?: ")
	complete = input("Does it have everything?: ")
	nib = input("Is it new in box?: ")
	insert(title, upc, system, value, complete, nib)


def view():
	con = sqlite3.connect("gamesData.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM games")
	rows=cur.fetchall()	
#	con.commit()  Not needed when fetching data
	con.close()
	return rows

table = view()

for i in table:
	print(i)

print(table[1])







