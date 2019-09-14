
import re
import My_CalculatorBE


print("This is a Python Calculator Script")

prev = 0
run = True

def performMath():
	global run #use a var outside of function
	global prev
	equation =""
	
	
	if prev == 0:
		equation = input("Enter equation")
	else:
		equation = input(str(prev))
	
	if equation == "quit":
		print("GoodBye!!")
		run = False
	else:
		equation = re.sub('[a-zA-Z,.:()" "]','',equation)
		
		if prev == 0:
			prev = eval(equation)   #eval is part of re package
		else:
			prev = eval(str(prev) + equation)
			
		
		print("You typed", prev)





#keeps programing going until run is set to false
while run:
	performMath()
	







