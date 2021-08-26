'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1): 
    print("* "*n)'''

'''n=int(input("Enter the number of rows: ")) #n=5
for i in range(1,n+1): #i=1  , n=6
    for j in range(1,n+1): # j=1
        print(i,end=" ")
    print()'''

'''n=int(input("Enter the number of rows: ")) #5
for i in range(1,n+1): #i=1
    for j in range(1,n+1): #j=2
        print(chr(64+i),end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i,end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,1+i): 
        print("*",end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print("*"*i)'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,1+i):
        print(i,end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,1+i):
        print(j,end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,1+i):
        print(chr(64+i),end=" ")
    print()'''

'''import time
n=int(input("Enter the number of rows: "))
for i in range(3,n+1):6
time.sleep(1)
for j in range(1,n+2-i): 4
time.sleep(1)
print("*",end=" ")
print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+j),end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n+1-i,end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n+1-j,end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(65+n-i),end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),"*"*i,end=" ")
    print() '''

'''import time
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1, i+1):
        time.sleep(1)
        print("*",end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1, i+1):
        print(i,end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1, i+1):
        print(j,end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1, i+1):
        print(chr(64+i),end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1, i+1):
        print(chr(64+j),end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(1, n+2-i):
        print(i,end="")
    print()'''

''''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(1, n+2-i):
        print(j,end="")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(1, n+2-i):
        print(chr(64+i),end="")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(1, n+2-i):
        print(chr(64+j),end="")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i):
        print(i-j,end=" ")
    for k in range(0,i):
        print(k,end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i):
        print(chr(i-j+65),end=" ")
    for k in range(0,i):
        print(chr(k+65),end=" ")
    print()
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''

'''for k in range(1,n+1):
    print(" "*k,end=" ")
    for l in range(1,n+1-k):
        print("*", end=" ")
    print()

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(i ,end=" ")
    print()

for k in range(1,n+1):
    print(" "*k,end=" ")
    for l in range(1,n+1-k):
        print(k, end=" ")
    print()'''


'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(chr(64+i) ,end=" ")
    print()

for k in range(1,n+1):
    print(" "*k,end=" ")
    for l in range(1,n+1-k):
        print(chr(64+k), end=" ")
    print()  '''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for k in range(1,n+1):
    for l in range(1,n+2-k):
        print("*",end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
for k in range(1,n+1):
    for l in range(1,n+2-k):
        print(k,end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
for k in range(1,n+1):
    for l in range(1,n+2-k):
        print(chr(64+k),end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(1,i):
        print("*",end=" ")
    print()

for k in range(1,n+1):
    print(" "*(n-k),end=" ")
    for l in range(1,k+1):
        print("*",end=" ")
    print()'''

'''import time
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    time.sleep(1)
    for j in range(i,n+2-i):
        print(j,end=" ")
    print()

for k in range(1,n+1):
    print(" "*(n-k),end=" ")
    time.sleep(1)
    for l in range(1,k+1):
        print(k,end=" ")
    print()'''


#nterms = int(input("How many terms? "))

# first two terms
'''n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1'''

'''i=1
whlie i<6:
    print(i)
    i+=1'''

'''n=int(input("enter the number  of rows:"))
for i in range(1,n+1):#i=1
    for j in range(1,n+1):#j=2
        print(chr(64+i),end=" ")
        print()'''

 '''for.ch.in.'Surya vandana':#ch=0,1...,2,3,4
    print(ch)
    if ch=='r' or ch=='d':
        break
    print('current letter:',ch)'''





    






