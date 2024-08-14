# # List comprehension in Python
# # It is used in simple not in complex statements


# # Task
# # approach 1
# a=[1,2,3,4,5]
# b=[]
# for i in a:
#     b.append(i**2)

# print(b)
# # approach 2
# b=[element**2 for element in a]
# print(b)

# output=[i**2 if i%2==0 else i**3 for i in range(1,100) ]
# print(output)

# # Generators in python
# # -- special type of function that returns multiple values 
# # -- yield is used
# # -- variable is not save also used to reduce the waste of memory . memory management

# #simple generator

# def generator_function():
#     yield 'a'
#     yield 'b'

# # ------approach 1----
# x=generator_function()
# print(next(x))
# print(next(x))
# # ------approach 2------

# for value in generator_function():
#     print(value)


# # Generator expression

# square_generator=(x**2 for x in range(0,10))
# print(list(square_generator))

# # Task --

# generator_operator=(number for number in range(1,100) if number%2==0)
# while True:
#     try:
#         display=input("type next to display\n")
#         if(display=='next'):
#             print(next(generator_operator))
#         else:
#             print(generator_operator)
#     except:
#         print("bye")
#         break

# # Lamda function
# # -- annonymus function used for short operation and also reduce the memory

# x=lambda parameter:parameter**2 
# print(x(7,7))

# x=lambda parameter:parameter*0.5
# list1=[1,2,3,4,5,6]
# for l in range(0,len(list1)):
#     print(x(l))

# greater_number=lambda x,y:x if x>y else y
# print(greater_number(5,9))

## task

import pandas as pd

list_variable=[]


n=int(input("enter number of element in list\n"))
for i in range(0,n):
    x=input("enter numbers\n")
    list_variable.append(x)

odd_even_checker=lambda parameter:"even" if parameter%2==0 else "odd"

odd_even_list=[odd_even_checker(i) for i in range(0,n)]


df = pd.DataFrame({
    "Number": list_variable,
    "Even/Odd": odd_even_list
})

print(df)