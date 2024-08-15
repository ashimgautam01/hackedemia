import pandas as pd

# list1=[1,8,9,0]
# x=int(input("enter any number to add to the list\n"))
# list1.append(x)
# print(list1)

dict1={
    "name":[],
    "address":[]
}
n=int(input("enter the number of students\n"))
for i in range(0,n):
    input_name=input("enter name \n")
    input_address=input("enter your address\n")
    dict1["name"].append(input_name)
    dict1["address"].append(input_address)

df=pd.DataFrame(dict1)
df.to_csv("new.csv",index=False)
print(df)