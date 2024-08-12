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

def TOH( n, sour, aux, des):
    if(n==1):
        print(f'move disk {n} from{sour} to {des}\n')
    else:
        TOH(n-1,sour,des,aux)
        print(f'move disk {n} from{sour} to {des}\n')
        TOH(n-1,aux,sour,des)

x=int(input("Enter a number\n"))
TOH(x,'A','B','C')

list =[1,2,4,5,7,8]
list.insert(3,6)
list.remove(4)
print(list)
def print_even(list):
    for i in range(0,len(list)):
        if(list[i]%2==0):
            print(list[i])

print_even(list)

dict_1={
    "key 1":70,
    "key 2":80
}
print(dict_1)

dict_2={
    "key 1":{"key 01":"ashim"},
    "key 2":"apple"
}
print(dict_2)

key_list={"key 1","key 2","key 3"}
value_list={"apple","banana","mango"}
dict_3=dict(zip(key_list,value_list))
print(dict_3)

keys=[]
values=[]
while True:
    x=input("enter a key value\n")
    y=input("enter a value\n")
    keys.append(x)
    values.append(y)
    dec=input("do you want to continue if yes type y and n for no\n").lower()
    if dec in ('no','n'):
        break
    else:
        continue
    
print(x)    
dict_4=dict(zip(keys,values))
print(f'dictionary:{dict_4}')

keylist=["key 1","key 2","key 3"]
valuelist=["ashim","gautam","don"]
dict1=dict(zip(keylist,valuelist))
print(dict1)

