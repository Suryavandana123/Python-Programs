'''def add(): #called function
    a=int(input("enter first value"))
    b=int(input("enter second value"))
    print(a+b)
    add()#calling function'''

'''import time
def add(): #called function
    a=int(input("enter first value"))
    b=int(input("enter second value"))
    print(a+b)
    time.sleep(2)

add()#calling function
print("first time call completed")
add()
print("second time call completed")
add
print("third time call completed")'''

'''def info(first_nam,Last_name): #called function
    print("first name=",first_name)
    print("second name=",second_name)
    info("vandana","atreyapurapu")'''

'''def addition(val):#called func
    print("addition of two no=",val+val)

    addition(5)#calling func
    addition(10)'''

'''#positional argument passing in correct 
def add(num1,num2):
    return num1+num2
    print(add(2,3))#called function'''

'''def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("enter a number: "))
print(factorial(n))'''

'''def sum(x,y):
    return x+y

a= int(input("Enter first number:"))
b= int(input("Enter second number:"))
print("Sum of the given two numbers is: ", sum(a,b))'''

'''def diff(x,y):
    return x-y

a=int(input("enter first number"))
b=int(input("enter second number"))
print("diff of given two numbers is:",diff(a,b))'''

'''def largest(x, y):
    if x > y:
        return x
    else:
        return y
x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
result = largest(x, y)
print("Largest is:", result)'''

'''def smallest(x,y):
    if x<y:
        return x
    else:
        return y
x=int(input("enter first number"))
y=int(input("enter second number"))
result=smallest(x,y)
print("smallest is:",result)'''

'''# Function for fibonacci

def fibonacci(n):
	a = 0
	b = 1
	
	# Check is n is less
	# than 0
	if n < 0:
		print("Incorrect input")
		
	# Check is n is equal
	# to 0
	elif n == 0:
		return 0
	
	# Check if n is equal to 1
	elif n == 1:
		return b
	else:
		for i in range(1, n):
			c = a + b
			a = b
			b = c
		return b
print(fibonacci(9))'''

'''def func(name):# called function ["Vandana","Garima","Sonal","Rahul"]
    for i in (name): #i=0,1,2,3,4
     print(i)

name_of_p=["vandana","Garima","Sonal","Rahul"]
func(name_of_p)#calling function'''

'''mydict={
    101: "Vandana",
    102: "Garima",
    103: "Sonal",
    104: "Rahul"
}
print(mydict)

for x in mydict.values():
    print(x)'''