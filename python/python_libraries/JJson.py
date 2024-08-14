import json

# dict1={
#     "students":["ashim","ram","sita"],
#     "marks":[10,20,30]
# }

# with open('data.json','w') as f:
#     json.dump(dict1,f)
    
# with open('data.json','r') as f:
#     output=json.load(f)

# print(output)

# dict1={
#     "username":[],
#     "password":[],
#     "phone":[]
# }

# print("1:sign up\n")
# print("2:sign in\n")
# print('3:exit')
# x=int(input("Enter 1 or 2\n"))
# match x:
#     case 1:
#         username=input("enter username\n")
#         password=input("enter password\n")
#         phone=input("enter mobile number")
#         dict1["username"].append(username)
#         dict1["password"].append(password)
#         dict1["phone"].append(phone)
#         with open('login.json','w') as f:
#             json.dump(dict1,f)
#     case 2:
#         username=input("enter username\n")
#         password=input("enter password\n")
#         with open('login.json','r') as f:
#             out=json.load(f)
#         for user in out:
#             if user["username"] ==username:
#                 if user["password"]==password:
#                     print(f'hello {username}')
#         else:
#             print('invalid')


dictionary={
    "name":[],
    "address":[],
    "mobile":[]
}

print("1 : Write\n")
print("2 :Read\n")
choice=int(input("enter 1 or 2\n"))
if choice==1:
    user_name=input("enter name\n")
    user_address=input("enter address\n")
    user_mobile=input("enter mobile number\n")
    dictionary["name"].append(user_name)
    dictionary["address"].append(user_address)
    dictionary["mobile"].append(user_mobile)
    with open('new.json','a') as f:
        json.dump(dictionary,f)
else:
    with open('new.json','r') as f:
        print(json.load(f))

        