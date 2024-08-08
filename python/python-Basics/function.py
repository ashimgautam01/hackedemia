x=int(input("enter a number\n"))
def add(x):
    if(x>0):
        print(f'{x} is a positive number\n')
    elif(x==0):
        print(f'{x} is 0')
    else:
        print(f'{x} is negative\n')
add(x)

x=int(input("enter a number\n"))
def function(x):
    if(x%10==0):
        return f'{x} is a multiple of 10\n'
    else:
        return f'{x} is not multiple of 10\n'
print(function(x))

x=int(input("enter a number\n"))

def even_checker(x):
    if(x%2==0):
        return "number is a even number\n",x
    else:
        return f'{x} is not a even number\n'

print(even_checker(x))
print(even_checker(5))

num=int(input("Enter a number\n"))
def sum(num):
    if(num==0):
        return 0
    else:
        return num+sum(num-1)
    
print(sum(num))    

x=input("Enter a string\n")

print(x.lower())