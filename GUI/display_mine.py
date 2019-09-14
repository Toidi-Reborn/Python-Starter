
import sqlite3
from tkinter import *  #all

window = Tk()  #need


def create_table():

	con = sqlite3.connect("gamesData.db")
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS games (item TEXT, upc, console TEXT, price REAL, complete, nib)") #create table with columns
	con.commit()
	con.close()
	
def insert():
	con = sqlite3.connect("gamesData.db")
	cur = con.cursor()
	#cur.execute("INSERT INTO games VALUES ('Madden', 2, 1.25)")	
	#cur.execute("INSERT INTO games VALUES (?,?,?,?,?,?)", (title, upc, system, value, complete, nib))	
	title = lg1_value.get()
	upc = lg2_value.get()
	system = lg3_value.get()
	value = lg4_value.get()
	complete = lg5_value.get()
	nib = lg6_value.get()
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

#for i in table:
#	print(i)

#print(table[1])


def km_to_mi():
	print("Success!!")
	print(e1_value.get())
	miles = float(e1_value.get()) * 1.6
	print(miles)
	miles = round(miles, 10)
	t1.delete(1.0,END)
	t1.insert(END, miles)


########## Window Frame

window.title("This is the Title Bar!!!!")
window.geometry("500x300") #size of the window


########## Row 0


head = Label (window, text="Convert KM to Miles")
head.grid(row=0, column=0, columnspan = 5)

########## Row 1


bkLine = Label(window, text = "")
bkLine.grid(row=1, column=0)

########## Row 2

l = Label(window, text = "Enter KM: " , bg="blue", fg = "white")
l.grid(row=2, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row=2,column=1)

b1 = Button(window, text="Convert!", command=km_to_mi)
b1.grid(row=2,column=2)  #or pack

########## Row 3

l1 = Label(window, text = "Miles:")
l1.grid(row=3, column=0)

t1 = Text(window,height=1,width=10)
t1.grid(row=3, column=1, columnspan=1)

########## Row 4

bkLine2 = Label(window, text = "")
bkLine2.grid(row=4, column=0)

	#insert(title, upc, system, value, complete, nib)

lg1 = Label (window, text = "Title: ")
lg1.grid(row=5, column = 0)
lg1_value = StringVar()
lg1b = Entry(window, textvariable = lg1_value)
lg1b.grid(row=5,column=1)

lg2 = Label (window, text = "UPC: ")
lg2.grid(row=6, column = 0)
lg2_value = StringVar()
lg2b = Entry(window, textvariable = lg2_value)
lg2b.grid(row=6,column=1)

lg3 = Label (window, text = "System: ")
lg3.grid(row=7, column = 0)
lg3_value = StringVar()
lg3b = Entry(window, textvariable = lg3_value)
lg3b.grid(row=7,column=1)

lg4 = Label (window, text = "Value: ")
lg4.grid(row=8, column = 0)
lg4_value = StringVar()
lg4b = Entry(window, textvariable = lg4_value)
lg4b.grid(row=8,column=1)

lg5 = Label (window, text = "Complete: ")
lg5.grid(row=9, column = 0)
lg5_value = StringVar()
lg5b = Entry(window, textvariable = lg5_value)
lg5b.grid(row=9,column=1)

lg6 = Label (window, text = "NIB: ")
lg6.grid(row=10, column = 0)
lg6_value = StringVar()
lg6b = Entry(window, textvariable = lg6_value)
lg6b.grid(row=10,column=1)




b2 = Button(window, text="Add to DB", command=insert)
b2.grid(row=11,column=0)






window.mainloop()   #need
