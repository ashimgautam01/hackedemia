## class collection of data member and member function


# class Animal:
#     def What_To_Do(self,flag):
#         if flag.lower() == "bark":
#             print("It is a dog")
#         elif flag.lower() == "meow":
#             print("It is a cat")
#         else:
#             print("It Talks")

# species_1=Animal()
# species_1.What_To_Do("bark")
# species_2=Animal()
# species_2.What_To_Do("mew")
x=7
y=8

# class Calculator:
#     def Addition(x,y):
#         print(f'{x}+{y}={x+y}')
#     def Substraction(x,y):
#         print(f'{x}-{y}={x-y}')

# operation=Calculator
# operation.Addition(x,y)
# operation.Substraction(x,y)


# class KBC:
#     def __init__(self,username):
#         print(f'welcome{username}')

# x=KBC('Ashim')


class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

species_1=Animal('Dog',18)