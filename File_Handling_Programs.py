'''f=open("myfile.txt","w")
print("name of the file",f.name)
print("filemode",f.mode)
print("readeable",f.readable)
f.close'''

'''f=open("covid.txt","w")
f.write("Vandana is the university topper")
print("written work has done successfully")
f.close'''

'''f=open("covid.txt","w")
mylist=["Surya","Vandana","pythonclass"]
f.writelines(mylist)
f.close

f=open("covid.txt","r")
print(f.read())
print(f.read(5))
print(f.readline())
print(f.readlines())'''

'''with open("myfile.txt","w") as f:
    f.write("amit\n")
    f.write("Vandana\n")
    print("file closed:",f.closed)
print("file closed:",f.closed)'''

'''f=open("myfile.txt","r")
print(f.tell())

print("total data",f.read())
print(f.tell())
f.seek(5)'''

'''f1=open("flowers.jpg","rb")
f2=open("flowers2.jpg","wb")
data=f1.read()
f2.write(data)'''

'''import csv
f=open("student.csv","w",newline="")
a=csv.writer(f)
b=int(input("enter the no of student"))
a.writerow(["rollno","name","mobileno","email","address","paper1","paper2","paper3","paper4","paper5","total","percentage","result","grade"])
for i in range(1,b+1):
    rollno=int(input("enter the roll no"))
    name=input("enter the name")
    mobileno=int(input("enter the mobileno"))
    email=input("enter the email")
    address=input("enter the address")
    paper1=int(input("enter the marks"))
    paper2=int(input("enter the marks"))
    paper3=int(input("enter the marks"))
    paper4=int(input("enter the marks"))
    paper5=int(input("enter the marks"))
    total=paper1+paper2+paper3+paper4+paper5
    percentage=(total/500)*100
   
    a.writerow([rollno,name,mobileno,email,address,paper1,paper2,paper3,paper4,paper5,total,percentage])
print("student record has save")'''



