#  Day 1 Basics Of Python

print("hello world")
x=75
print(x)
a='ashim'
b='gautam'
print(a+b)

x=10
y=20
print(f'addition:{x+y}\n substraction:{x-y}\nMultipication:{x*y}\nDiviision:{x/y}')

x=int(input("enter a number\n"))
y=int(input("enter another number\n"))

print(f'Mathmatical operation of {x} and {y}\nadd:{x+y}\nsubs:{x-y}')

p=int(input("Enter principal\n"))
time=float(input("Enter Time\n"))
r=float(input("Enter rate\n"))
si=p*time*r/100
print(f'The simple interest of {p} {time} and {r} is\t {si}')

def simple(p,time,r):
    si=p*time*r/100
    print(f'The simple interest of {p} {time} and {r} is\t {si}')

simple(p,time,r)
