'''a=int(input("enter first number"))
b=int(input("enter second number"))
print(a/b)'''

'''a=int(input("enter first number"))
b=int(input("enter second number"))
try: print(a/b)
except:
    print(" you can not divide any number by zero")'''

'''a=int(input("enter first number"))
b=int(input("enter second number"))
try: 
    print(2/0)
except:
    print("the description of exception:",message)'''

'''a=int(input("enter any one number a="))
b=int(input("enter second number b="))
try: 
    b>a
    print("b is greater than a")
except:
     a==b
     print("a and b are equal")'''

'''a=int(input("enter an age"))
age=18
try:
    a>=18
    print("you are eligible")

except:
    a<18
    print("you are not eligible")'''

'''#WAP to reverse 3 numbers
num=int(input("enter three number"))
a=num%10 #a=3 123%10
num=num//10 #num=12 |123//10=12
#print(a)
b=num%10 #12 |123//10=12
c=num%10 #c=1
rev=a*100+b*10+c*1 #(3*100=321)
print("reverse= ",rev)'''

'''#WAP to reverse 5 numbers
num=int(input("enter five number"))
a=num%10 #a=5 12345%10
num=num//10 #num=1234 |12345//10=1234
#print(a)
b=num%10 #1234 |12345//10=12
c=num%10 #c=1
rev=a*100+b*10+c #(5*100=54321)
print("reverse= ",rev)'''

'''#WAP to reverse 7 numbers
num=int(input("enter seven number"))
a=num%10 #a=7 1234567%10
num=num//10 #num=123456 |1234567//10=123456
#print(a)
b=num%10 #123456 |1234567//10=12345
c=num%10 #c=1
rev=a*100+b*10+c #(7*100=7654321)
print("reverse= ",rev)'''

'''#armstrong number
def number(n):
    temp=n #153
    sum=0 #0 
    while(temp!=0):
        rm=temp%10
        sum=sum+(rm*rm*rm)
        temp=temp//10
    print(sum)
    return (sum==n)
n= int(input("enter numbet to check it is armstrong number or not"))
print(number(n)) #calling function'''

#a=int(input("enter first integer"))
#b=int(input("enter second integer"))
#multiple except block
'''try:
    a=int(input("enter first integer"))
    b=int(input("eneter second integer"))
    print(a/b)
except ZeroDivisionError as message:
    print("plz ensure that you can't divide any no by  zero:",ZeroDivisionError)
except ValueError as message:
    print("enter only integer no=>",message)'''

'''#Handling multiple diffrent kinds of exception with single except block
try:
   a=int(input("enter first number"))
   b=int(input("enter second number"))
   print(a/b)
except (ValueError,ZeroDivisionError) as messaage:
     print("enter correct number:")'''

'''try:
   a=int(input("enter first number"))
   b=int(input("enter second number"))
   print(a/b)
except (ValueError,ZeroDivisionError) as messaage:
     print("enter correct number:")
else:
    print("Everything is ok")'''

'''try:
   a=int(input("enter first number"))
   b=int(input("enter second number"))
   print(a/b)
except (ValueError,ZeroDivisionError) as messaage:
     print("enter correct number:")
finally:
      print("I will always execute")'''

#Nested try except block
'''try:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    try:
        print(a/b)
    except ZeroDivisionError as msg:
        print(msg)
except ValueError as msg:
    print(msg)'''

#user defined exception by raise keyword
'''obj=50
if obj>40:
       raise Exception("value 40 is not greater than 50")'''

'''#python logging
import logging
logging.basicConfig(filename="newfile.txt",level=logging.DEBUG)
logging.debug("this indicates the debugging information")
logging.info("this indicates the imortant information")
logging.error("this indcates error information")
logging.warning("this indicates the warning information")
logging.critical("this indicates the critical infrmation")'''

'''import logging
logging.basicConfig(filename="newexception.txt",level=logging.DEBUG)
try:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    print(a/b)
except(ZeroDivisionError, ValueError) as message:
    print(message)
    logging.exception(message)'''


































