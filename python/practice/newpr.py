# import pandas as pd

# # list1=[1,8,9,0]
# # x=int(input("enter any number to add to the list\n"))
# # list1.append(x)
# # print(list1)

# dict1={
#     "name":[],
#     "address":[]
# }
# n=int(input("enter the number of students\n"))
# for i in range(0,n):
#     input_name=input("enter name \n")
#     input_address=input("enter your address\n")
#     dict1["name"].append(input_name)
#     dict1["address"].append(input_address)

# df=pd.DataFrame(dict1)
# df.to_csv("new.csv",index=False)
# print(df)


# # map filter and reuce decorator

# list1=[1,2,3,4,5]
# def mapelements(x):
#     return x*x

# print(list(map(mapelements,list1)))

# list2=[1,2,3,4,5,6]
# list3=[7,8,1,2,4,6]
# def filterelements(x):
#         return x

# print(list(filter(filterelements,list2)))

# def smartDecorator(func):
#     def wrapper(x,y):
#         return func(int(x),int(y))
#     return wrapper

# @smartDecorator
# def functionToAdd(x,y):
#     return x+y

# print(functionToAdd('7','9'))


numbers=[1,2,3,4,5,6]
x=lambda x:x*x,numbers
for l in range(0,len(numbers)):
    print((l))