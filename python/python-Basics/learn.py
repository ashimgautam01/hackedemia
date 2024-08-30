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
