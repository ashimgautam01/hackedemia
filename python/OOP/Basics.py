## class collection of data member and member function


class Animal:
    def What_To_Do(self,flag):
        if flag.lower() == "bark":
            print("It is a dog")
        elif flag.lower() == "meow":
            print("It is a cat")
        else:
            print("It Talks")

species_1=Animal()
species_1.What_To_Do("bark")
species_2=Animal()
species_2.What_To_Do("mew")
x=7
y=8

class Calculator:
    def Addition(x,y):
        print(f'{x}+{y}={x+y}')
    def Substraction(x,y):
        print(f'{x}-{y}={x-y}')

operation=Calculator
operation.Addition(x,y)
operation.Substraction(x,y)


class KBC:
    def __init__(self,username):
        print(f'welcome{username}')

x=KBC('Ashim')


class Animal:
    def __init__(self):
        self.name=input("Enter name of animal\n")
        self.age=int(input("Enter age of animal\n"))
    
    def printDetails(self):
        print(f'Name:{self.name}\nAge: {self.age}')

    
species_1=Animal('Dog',18)
species_2=Animal('cat',78)
species_2.printDetails()
species_1.printDetails()
newsp=Animal
newsp.printDetails()


class User:
    def Welcome_User(self):
        print(f'Welcome {self.name}\n')
        print("1 Add note\n")
        print("2 Display ")
        print("3 Exit")
        n=int(input("enter number 1 or 2\n"))
        if n==1:
            self.Add_Note()
        elif n==2:
            self.ViewNote()
        elif n==3:
            exit()
        else:
            print("invalid number")
    def Add_Note(self):
        print(f'Hey {self.name} Enter note here\n')
        self.note=input("enter note here\n")
        print("note added successfully")
    def ViewNote(self):
        print(f'Hey {self.name} Enter note here\n')
        print(self.note)
    def Signup(self):
        self.name=input("enter name\n")
        self.password=input("enter password\n")
        self.mobile=int(input("enter mobile"))

    def Login(self):
        user=input("enter username")
        passw=input("enter password")
        if user==self.name and passw==self.password:
            self.Welcome_User()
        else:    
            print("Invalid Username or Password")

    def __init__(self):
        while True:
            print("1 Sign Up\n")
            print("2 Login ")
            n=int(input("enter number 1 or 2\n"))
            if n==1:
                self.Signup()
            elif n==2:
                self.Login()
               
            else:
                break

user=User()

