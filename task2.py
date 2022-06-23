def students():
    sub=[]
    num={}
   
print("number of students")
n=int(input())
students=[]
li=[]
for i in range(n):
    print("enter no. of subjects for student",(i+1))
    s=int(input())
    print("enter the subjects")
    li=[]
    for j in range(s):
        element=input()
        li.append(element)
    students.append(li)
print(students)




