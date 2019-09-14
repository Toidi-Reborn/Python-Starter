

import calendar
import time
import sqlite3



class Database:

	def __init__(self):   #initialize a object - only this is executed when a class is called
		self.con = sqlite3.connect("gamesData.db")
		self.cur = self.con.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS games (title, upc, system, value, complete, nib)") #create table with columns
		self.con.commit()

	def insert(self, title, upc, system, value, complete, nib):
		self.cur.execute("INSERT INTO games VALUES (?,?,?,?,?,?)", (title, upc, system, value, complete, nib))	
		self.con.commit()

	def view(self): 
		self.cur.execute("SELECT * FROM games")
		rows=self.cur.fetchall()	
	#	con.commit()  Not needed when fetching data
		return rows

	def lookup(self, title = "", UPC = "", System = "", Value = "", Complete = "", NIB = ""):
		self.cur.execute("SELECT * FROM games WHERE title = ? OR UPC = ? OR System = ? OR Value = ? OR Complete = ? OR NIB = ?" , (title, UPC, System, Value, Complete, NIB))
		self.rows = self.cur.fetchall()	
		return self.rows
		
	def delete(self, x):
		self.cur.execute("DELETE FROM games WHERE Title = ?", (x,))
		self.con.commit()

	def __del__(self):
		self.con.close()
		print("end")


