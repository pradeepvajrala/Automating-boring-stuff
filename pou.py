n=int(input("Enter number of students: "))

arr=[[input("Enter student's name: "),float(input("Enter students's marks: "))] for _ in range(0,n)]
arr.sort(key=lambda x: (x[1],x[0]))
names = [i[0] for i in arr]
marks = [i[1] for i in arr]
min_marks=min(marks)
while marks[0]==min_marks:
    marks.remove(marks[0])
    names.remove(names[0])
for x in range(0,len(marks)):
    if marks[x]==min(marks):
        print("Students with least marks are: "+ names[x])
