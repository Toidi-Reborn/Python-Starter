

import calendar
import time
import sqlite3



class Database:

	def __init__(self):   #initialize a object - only this is executed when a class is called

		con = sqlite3.connect("gamesData.db")
		cur = con.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS games (title, upc, system, value, complete, nib)") #create table with columns
		con.commit()
		con.close()
	
	def insert(self, title, upc, system, value, complete, nib):
		con = sqlite3.connect("gamesData.db")
		cur = con.cursor()	
		cur.execute("INSERT INTO games VALUES (?,?,?,?,?,?)", (title, upc, system, value, complete, nib))	
		con.commit()	
		con.close()

	def view(self):
		con = sqlite3.connect("gamesData.db")
		cur = con.cursor()
		cur.execute("SELECT * FROM games")
		rows=cur.fetchall()	
	#	con.commit()  Not needed when fetching data
		con.close()
		print (rows)
		return rows

	def lookup(self, title = "", UPC = "", System = "", Value = "", Complete = "", NIB = ""):
		con = sqlite3.connect("gamesData.db")
		cur = con.cursor()
		cur.execute("SELECT * FROM games WHERE title = ? OR UPC = ? OR System = ? OR Value = ? OR Complete = ? OR NIB = ?" , (title, UPC, System, Value, Complete, NIB))
		rows=cur.fetchall()	
		con.close()
		return rows


	def delete(self, x):
		con = sqlite3.connect("gamesData.db")
		cur = con.cursor()
		cur.execute("DELETE FROM games WHERE Title = ?", (x,))
		con.commit()
		con.close()






			
