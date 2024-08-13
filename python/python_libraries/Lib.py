import pandas as pd

dict1={
    'student':['ram','ashim',"shyam"],
    'marks':[80,78,12],
    'address':["pokhara","kathmandu","parbat"],
}
data_frame=pd.DataFrame(dict1)  #convert dictionary into dataframe print in the form of table

data_frame['age']=[21,15,29]  # adding data to table

print(data_frame)

# Removing
newframe=data_frame.drop(columns=['marks'])

print(newframe)


dict1={
"question":[],
"answer":[]
}
n=int(input("print number of questions\n"))
for i in range(1,n+1):
    question=input(f'enter question no {i}\n ')
    answer=input(f'enter answer of quesstion {i}\n')
    dict1["question"].append(question)
    dict1["answer"].append(answer)

dict_frame=pd.DataFrame(dict1)
print(dict_frame)

n=int(input("enter number of students\n"))

dict1={
    "name":[],
    "marks":[]
}

for i in range(1,n+1):
    name=input(f'Enter name of student {i}\n')
    mark=int(input(f'Enter marks of student {i}\n'))
    dict1["name"].append(name)
    dict1["marks"].append(mark)


dict_frame=pd.DataFrame(dict1)
print(dict_frame)

print("\npassed student\n")

#  look up in table

fail_std=dict_frame.loc[(dict_frame['marks']<=40)]

print(fail_std)

# to store in csv file
dict_frame.to_csv('data.csv',index=False)

#to read from csv
read=pd.read_csv('data.csv')

print(read)
print(read.loc[dict_frame["marks"]>50])

# To print the certain index
print(read.iloc[1])



