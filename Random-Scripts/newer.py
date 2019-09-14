

testSplit = "this.is.just.a.test"

print("(testSplit)")
print (testSplit)
print()

print("(testSplit.split('.'))")
print (testSplit.split("."))
print()


print("(testSplit.split('.')[2])")
print (testSplit.split(".")[2])
print()

print("for each in split")
arr = testSplit.split('.')
for i in arr:
	print(i)
print()



print("passing variables")
def printSomething(name = "default", age = 33):
	print("Hi, My name is " + str(name) + " and I am " + str(age))
	#either or
	print("Hi, My name is",name,"and I am", age)
		
printSomething(age = 23, name = "Jeff")
print()



print("")
def doMath(num1, num2):
	return num1 + num2

math1 = doMath(5,7)
math2 = doMath(11, 44)
print("First is ", math1, "and the 2nd is ", math2)
print()
print()

print("If / Else code")
check = "Cheeseburger"
if check == False:
	print("Check is False")
elif check == "Cheeseburger":
	print("Yummy")
else:
	print("Check is not False")
print()


print("for loop code")
numbers = [1,2,3,4,5]
for i in numbers:
	print("The number is", i)
	
	
print()
	

print("While Loop Code")

run = True
current = 1

while run:    #while run is True
	if current == 20:
		run = False
	else:
		print(current)
		current += 1

print()
print()


import re  #reggex??

string = "I AM NOT yelling 4 but we know 77 it is true"
print(string)
newString = re.sub('[A-Z]','',string)
print(newString)
newString2 = re.sub('[a-z]','',string)
print(newString2)
newString3 = re.sub('[" "]','',string)
print(newString3)
newString4 = re.sub('[0-9]','NUMBER DELETED',string)
print(newString4)
newString5 = re.sub('[^0-9]','?',string)
print(newString5)

