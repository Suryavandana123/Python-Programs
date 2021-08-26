'''age=18
if age>=18:
    print("you re eligible")

else:
    print("you are not eligible")'''

''' age=16
if age>=18:
    print("you re eligible")

else:
    print("you are not eligible")'''

'''a=int(input("enter any one number a="))
b=int(input("enter second number b="))
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")'''

'''brand= input("Enter your cold drink name")
if brand== "pepsi" or brand== "PEPSI":
    print("Swag")
elif brand== "dew" or brand=="DEW":
    print("Dar ke aage jeet hain")
elif brand=="thumsup" or brand=="THUMSUP":
    print(" Taste the thunder ")
else:
    print("Go with your brand")'''

'''num=int(input("enter a number"))
factorial=5
if num<0:
    print("factorial does not exist for negative number")
elif num==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
      factorial=factorial*i
      print("the factorial of",num,"is",factorial)'''

'''def fibonacci(n):
    if n<0:
        print("incorrect input")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
        else:
        return fibonacci(n-1)+ fibonacci(n-2)
print(fibonacci(9))'''
        
'''a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
if a>b:
    if a>c:
        print("A is greater")
    else:
        print("C is greater")
else:
    if b>c:
        print("B is greater")
    else:
        print("C is greater")'''

'''#WAP to check if year is a leap year or not
year=int(input("Enter a year:"))
if(year % 4)==0:
        if(year % 400)==0:
            print("the year is a leap year")
else:
    print("the year is not a leap year")'''

'''a=int(input("enter the value of a"))
b=int(input("enter the value of b"))b
c=int(input("enter the value of c"))
if a<b:
    print("b is greater")
    if a<c:
        print("C is greater")
else:
    print("C is greater")

if b<c:
    print("C is greater")

else:
    print("B is greater")'''

'''#wap practicle marks

p1=int(input("enter the marks of Maths"))
p2=int(input("enter the marrks of Eglish"))
p3=int(input("enter the marks of science"))
p4=int(input("enter the marks of Chemistry"))
p5=int(input("enter the marks of Hindi"))
practical1=int(input("enter the mark of physics practical"))
practical2=int(input("enter the marks of Chemistry practical"))
a=p1+p2+p3+p3+p4+p5+practical1+practical2;
b=(a/700.0)*10
#print (b)
#print(a)
print("total marks",a)
print("total marks",b)

if p1>40 and p2>40 and p3>40 and p4<40 and p5>40 and practical1>50 and practical2<50:
    print("grade D")

elif p1>40 and p2>40 and p3>40 and p4>40 and p5>40  and practical1>15 and practical2>20 and b>10 and b<=20:
    print("grade C")
 
elif P1>40 and P2>40 and P3>40 and P4>40 and P5>40 and  practical>15 and practical2>20 and b>40 and b<=60:
    print("grade B")

elif p1>40 and P2>40 and P3>40 and P4>40 and P5>40 and practical1>15 and practical2>20 and b>60 and b<=80:
    print("grade A")

elif p1> 40 and p2>40 and p3> and p4> and p5>40 and practical1>15 and practical2>20:
    print(" Grade= A+")
else:
    print(" Fail")'''

'''container=[2,1,4,5,5,4,4,1,1]
count=0
even=0
odd=0
for i in container:
    if i==4:
    count+=1
    elif i==2:
        even+=1
    elif i==5:
        odd+=1
print(count-even)
print(count-odd)'''

'''name=input("Enter name")
if name== "Vandana":
    print("Hello Iam Vandana and Iam an Engineer")
else:
    print("Did not match the pattern")'''

'''no= int(input("Enter any single number "))

if no>0:
    print("the number is positive")

if no<0:
    print("the number is negative")

if no==0:
    print("the number is zero")'''








  
    



