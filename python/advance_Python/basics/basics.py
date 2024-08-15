# List comprehension in Python
# It is used in simple not in complex statements


# Task
# approach 1
a=[1,2,3,4,5]
b=[]
for i in a:
    b.append(i**2)

print(b)
# approach 2
b=[element**2 for element in a]
print(b)

output=[i**2 if i%2==0 else i**3 for i in range(1,100) ]
print(output)

# Generators in python
# -- special type of function that returns multiple values 
# -- yield is used
# -- variable is not save also used to reduce the waste of memory . memory management

#simple generator

def generator_function():
    yield 'a'
    yield 'b'

# ------approach 1----
x=generator_function()
print(next(x))
print(next(x))
# ------approach 2------

for value in generator_function():
    print(value)


# Generator expression

square_generator=(x**2 for x in range(0,10))
print(list(square_generator))

# Task --

generator_operator=(number for number in range(1,100) if number%2==0)
while True:
    try:
        display=input("type next to display\n")
        if(display=='next'):
            print(next(generator_operator))
        else:
            print(generator_operator)
    except:
        print("bye")
        break

# Lamda function
# -- annonymus function used for short operation and also reduce the memory

x=lambda parameter:parameter**2 
print(x(7,7))

x=lambda parameter:parameter*0.5
list1=[1,2,3,4,5,6]
for l in range(0,len(list1)):
    print(x(l))

greater_number=lambda x,y:x if x>y else y
print(greater_number(5,9))

# task

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

# map function
# link or associate
# simply map one by one faster way to do the same task
# in map filter and reduce (function_name,iterable)

list1=[3,4,1,2,3,4]
output=list(map(lambda x:x*x,list1))
print(output)

def output_function(x,y):
    return x*x+y*y

list_a=[1,2,3,4]
list_b=[6,7,8,9]

print(list(map(output_function,list_a,list_b)))

list1=[]
list2=[]

def check_10(x,y):
    if(x+y)==10:
        return str(x)+str(y)

n=int(input("enter number of elements\n"))
for i in range(0,n):
    list_1=int(input("enter values for list 1\n"))
    list1.append(list_1)

for i in range(0,n):
    list_2=int(input("enter values for list 2\n"))
    list2.append(list_2)

print(list(map(check_10,list1,list2)))
        
#Filters

numbers_=[1,2,3,4,50]
print(list(filter(lambda x:x%2==0,numbers_)))

list_=["apple","dog","elephant","cat","dog"]

def length(x):
    if (len(x)>3):
        return x

print(list(filter(length,list_)))


# Reduce
from functools import reduce


list_number=[1,2,3,4,5,6]
output=reduce(lambda x,y:x*y,list_number)
print(output)

list1=[]
n=int(input("enter number of elments in list\n"))

def square_and_add(x):
    return x*x+4

def divide_check(x):
    if x%5==0:
        return x

for i in range(0,n):
    input_numbers=int(input("enter numbers in list\n"))
    list1.append(input_numbers)

list2=list(map(square_and_add,list1))
divide=list(filter(divide_check,list1))
sum=reduce(lambda x,y:x+y,list1)
print(sum)
print(divide)
print(list2)

#                                      Decorators
# speccial function that takes another function as a parameter
# used by @

def smart_conversion(func):
    def wrapper(x,y):
        return func(int(x),int(y))
    return wrapper
@smart_conversion
def function_divide(x,y):
    return x/y
@smart_conversion
def function_addition(x,y):
    return x+y

print(function_divide('4','2'))
print(function_addition('7','9'))


def decorator_function(func):
    def wrapper(x,y):
        print(f'{func.__name__} is running ')
        return func(int(x),int(y))
    return wrapper

@decorator_function
def function_addition(x,y):
    return x+y
@decorator_function
def function_substraction(x,y):
    return x-y
@decorator_function
def  function_devision(x,y):
    return x/y

print(function_substraction('7','10'))
print(function_addition('7','10'))
print(function_devision('7','10'))