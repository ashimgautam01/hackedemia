x=input("enter your name\n")

with open("file.txt",'a') as f:
    f.write(' '+x+' ')
with open('file.txt','r') as f:
    output=f.readlines()

print(output)

import json

dict1={
    "students":["ramji","ram","shyam"],
    "marks":[10,40,50]
}

with open('file.json','w') as f:
    students_name=input("enter student name\n")
    student_marks=input("enter students marks\n")
    dict1['students'].append(students_name)
    dict1["marks"].append(student_marks)
    json.dump(dict1,f)

with open('file.json','r') as f:
    output=json.load(f)
    name="ashim"
    if name in dict1["students"]:
        print("yes")
    else:
        print("no")