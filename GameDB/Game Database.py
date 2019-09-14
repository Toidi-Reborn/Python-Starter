"""
My Game DataBase
"""
from tkinter import *  #all
#from PIL import ImageTk,Image

import calendar
import time
import sqlite3
from GameBackEnd2 import Database


db = Database()

def clock():
	now = time.localtime(time.time())	
	timeM = " AM"
	
	timeHour = now.tm_hour
	if timeHour > 12:
		timeHour = now.tm_hour - 12
		timeM = " PM"
	timeMin = now.tm_min
	if timeMin < 10:
		timeMin = "0" + str(now.tm_min)
	timeSec = now.tm_sec
	if timeSec < 10:
		timeSec = "0" + str(now.tm_sec)

	now = str(now.tm_mon) + "/" + str(now.tm_mday) + "/" +  str(now.tm_year) + " " + str(timeHour) + ":" + str(timeMin) + ":" + str(timeSec) + str(timeM)
	timePH.configure(text = now)

	window.after(1000, clock)

def close():
	print("Program Closed by User")
	exit()


def dbToBox():
		box1.delete(0,END)
		table = db.view()
		for i in table:
			#print(i)
			box1.insert(END,i)

def search_command():
	sTitleR1.delete(0,END)
	sUPCR1.delete(0,END)
	sSystemR1.delete(0,END)
	sValueR1.delete(0,END)
	sCompleteR1.delete(0,END)
	sNIBR1.delete(0,END)
	for rows in db.lookup(searchBox.get(),searchBox.get(),searchBox.get(),searchBox.get(),searchBox.get(),searchBox.get()):
		sTitleR1.insert(END, rows[0])
		sUPCR1.insert(END, rows[1])
		sSystemR1.insert(END, rows[2])
		sValueR1.insert(END, rows[3])
		sCompleteR1.insert(END, rows[4])
		sNIBR1.insert(END, rows[5])

def getRow(event):#Bind the box to a line
	global selectedLine
	index = box1.curselection()
	selectedLine = box1.get(index)
	#return(selectedLine)  Not needed because var is global
	print (index[0])
	print (selectedLine)

def deleteS():
	db.delete(selectedLine[0])
	dbToBox()

def deleteTitle():
	delItem = lg7_value.get()
	con = sqlite3.connect("gamesData.db")
	cur = con.cursor()
	cur.execute("DELETE FROM games WHERE title=?",(delItem,))
	con.commit()
	lg7b.delete(0, END)
	con.close()
	dbToBox()

def addToList():
	title = lg1_value.get()
	upc = lg2_value.get()
	system = lg3_value.get()
	value = lg4_value.get()
	complete = lg5_value.get()
	nib = lg6_value.get()
	db.insert(title, upc, system, value, complete, nib)
	lg1b.delete(0, END)
	lg2b.delete(0, END)
	lg3b.delete(0, END)
	lg4b.delete(0, END)
	lg5b.delete(0, END)
	lg6b.delete(0, END)
	lg7b.delete(0, END)
	dbToBox()


#table = db.view()

#db.create_table()	

window = Tk()  #need


window.title("Game Database")

#window.geometry("500x500") #size of the window


# for cmd testing
now = time.localtime(time.time())	
nowX = str(now.tm_mon) + "/" + str(now.tm_mday) + "/" +  str(now.tm_year) + " " + str(now.tm_hour) + ":" + str(now.tm_min)
#print(nowX)
cal = calendar.month(2019, now.tm_mon)
print (cal)
# end cmd test


breakLine = Label(window, height = 1, text = "")
breakLine.grid(row=0, column=0)

lhead = Label (window, bg="black", fg="white", text = "Add Video Game To Database")
lhead.grid(row=1, column = 0, columnspan = 2)

lg1 = Label (window, text = "Title: ")
lg1.grid(row=2, column = 0)
lg1_value = StringVar()
lg1b = Entry(window, textvariable = lg1_value)
lg1b.grid(row=2,column=1)

lg2 = Label (window, text = "UPC: ")
lg2.grid(row=3, column = 0)
lg2_value = StringVar()
lg2b = Entry(window, textvariable = lg2_value)
lg2b.grid(row=3,column=1)

lg3 = Label (window, text = "System: ")
lg3.grid(row=4, column = 0)
lg3_value = StringVar()
lg3b = Entry(window, textvariable = lg3_value)
lg3b.grid(row=4,column=1)

lg4 = Label (window, text = "Value: ")
lg4.grid(row=5, column = 0)
lg4_value = StringVar()
lg4b = Entry(window, textvariable = lg4_value)
lg4b.grid(row=5,column=1)

lg5 = Label (window, text = "Complete: ")
lg5.grid(row=6, column = 0)
lg5_value = StringVar()
lg5b = Entry(window, textvariable = lg5_value)
lg5b.grid(row=6,column=1)

lg6 = Label (window, text = "NIB: ")
lg6.grid(row=7, column = 0)
lg6_value = StringVar()
lg6b = Entry(window, textvariable = lg6_value)
lg6b.grid(row=7,column=1)

b2 = Button(window, text="Add to DB", command = addToList)
b2.grid(row=8,column=0, columnspan =2)



#show database
b1 = Button(window, text="Show Data Base", bg="yellow", fg="blue", command = dbToBox) #showDB for print to cmd
b1.grid(row=9,column=0, columnspan =2)


#############################search

search = Label (window, text="Search")
search.grid(row = 11, column = 0)
search_value = StringVar()
searchBox = Entry(window, textvariable = search_value)
searchBox.grid(row=11, column = 1)

b4 = Button(window, fg = "black", bg = "white", text="Search", command=search_command)
b4.grid(row=12,column=0, columnspan = 2)
breakLine4 = Label(window, height = 1, text = "")
breakLine4.grid(row=13, column=0)


#delete
lg7 = Label (window, text="Enter Title to Delete")
lg7.grid(row=14, column = 0, columnspan = 2)
lg7_value = StringVar()
lg7b = Entry(window, textvariable = lg7_value)
lg7b.grid(row=15, column = 0, columnspan = 2)
b4 = Button(window, fg = "white", bg = "red", text="Delete Title", command = deleteTitle)
b4.grid(row=16,column=0, columnspan = 2)


#2nd section

colSpace1 = Label(window, width = 5)
colSpace1.grid(row = 0, column = 2)

#b5 = Button (window, text = "Print Time" , command = clock)
#b5.grid(row =1, column = 4, columnspan = 2, padx = 5)
timePH = Label (window, text = "Time Loading")
timePH.grid(row =1, column = 4, columnspan = 2)




# Box and scrollbar
scroll1 = Scrollbar(window)
scroll1.grid(row = 3, column = 3, rowspan = 10, sticky = NS)

box1 = Listbox(window, bg = "silver", height = 15, width = 30)
box1.grid(row = 3, column = 4, rowspan = 10, columnspan = 2)

box1.configure(yscrollcommand = scroll1.set)
scroll1.configure(command = box1.yview)

box1.bind('<<ListboxSelect>>' , getRow)


bDelete = Button(window, text = "Delete Selected", command = deleteS)
bDelete.grid (row = 13, column = 4, columnspan = 2)


#close
b6 = Button (window, text = "Close Window", bg = "red", fg = "yellow", command = close)
b6.grid(row =15, column = 4, columnspan = 2)


colSpace2 = Label(window, width = 5)
colSpace2.grid(row = 0, column = 6, rowspan = 14)


#start of 3rd section

#box3 = Listbox(window, bg = "red", height = 35, width = 10)
#box3.grid(row = 0, column = 7, rowspan = 16, columnspan = 1)   
#scroll3 = Scrollbar(window,  bg = "orange")
#scroll3.grid(row = 3, column = 8, rowspan = 10)
#box3.configure(yscrollcommand = scroll3.set)
#scroll3.configure(command = box3.yview)




#canvas and picture
can = Canvas(bg ="black", width = 185, height = 190)
can.grid(row = 0, rowspan = 15, column = 7)
gif = PhotoImage(file="img/s2.gif")
can.create_image(0,0, image = gif, anchor = NW)



#Search Results
lableData = Label(window, text = "Searched Title")
lableData.grid(row = 18, column = 0, columnspan = 9)

sTitle = Label (window, text = "Title")
sUPC = Label (window, text = "UPC")
sSystem = Label (window, text = "System")
sValue = Label (window, text = "Value")
sComplete = Label (window, text = "Complete?")
sNIB = Label (window, text = "NIB?")
sTitle.grid (row = 19, column = 0)
sUPC.grid (row = 19, column = 1)
sSystem.grid (row = 19, column = 2)
sValue.grid (row = 19, column = 4)
sComplete.grid (row = 19, column =5)
sNIB.grid (row = 19, column =6)

sTitleR1 = Listbox (window)
sUPCR1 = Listbox (window)
sSystemR1 = Listbox (window)
sValueR1 = Listbox (window)
sCompleteR1 = Listbox (window)
sNIBR1 = Listbox (window)
sTitleR1.grid (row = 20, column = 0)
sUPCR1.grid (row = 20, column = 1)
sSystemR1.grid (row = 20, column = 2)
sValueR1.grid (row = 20, column = 4)
sCompleteR1.grid (row = 20, column =5)
sNIBR1.grid (row = 20, column =6)


breakLineEnd = Label(window, height = 1, text = "")
breakLineEnd.grid(row=21, column=0)

clock()

dbToBox()


window.mainloop()   #need








