

from tkinter import *  #all

window = Tk()  #need

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











window.mainloop()   #need
