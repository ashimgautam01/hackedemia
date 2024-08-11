
x=int(input("enter a number\n"))
if (x%2==0) or (x==10):
    print(f'{x} is a even  number and number 10 \n')
elif(x!=10):
    print(f'{x} is not 10')
else:   
    print(f'{x} is a odd number nor 10\n')

realpass="pass"
username=input("enter username\n")
password=input("enter password\n")
if(realpass==password):
    print(f'welcome {username}\n')
else:
    print(f'sorry {username} you enter wrong password')
c=0
q1=input("which is capital of nepal\n")
if(q1=="kathmandu"):
    c=c+100
    print("correct answer")
    q2=input("which is capital of India\n")
    if(q2=="delhi"):
        c=c+100
        print("correct answer")
        q3=input("which is capital of england\n")
        if(q3=="london"):
            c=c+100
            print("correct answer")
        q4=input("which is capital of china\n")
        if(q4=="beijing"):
            c=c+100
            print("correct answer")
else:
    print("wrong answer")
    print(f'your score is {c}')
    exit()


for i in range(0,10):
    if(i%2!=0):
        print(i)
    else:
        continue    

while True:
    number=int(input("enter a number\n"))
    if(number %5==0):
        break
x=0
while x<5:
    print(x)
    x+=1

