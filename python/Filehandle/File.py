    # File handeling

# username=input("enter username\n")
# password=input("enter password\n")

# #writing in file
# with open('data.txt','w+') as f:
#     f.write('username:'+username+'  \n'+'password:'+password)

# Reading from file

# with open('data.txt') as f:
#     output=f.readlines()
#     print(output)

#task
# while True:
#     print("1:Write\n")
#     print("2:Read\n")
#     print('3:exit')
#     x=int(input("Enter 1 or 2\n"))
#     match x:
#         case 1:
#             note=input("enter your note\n")
#             with open('new.txt','a') as f:
#                 f.write(note)
#         case 2:
#             with open('new.txt','r') as f:
#                 output=f.readlines()
#                 for x in output:
#                     print(x)
#         case 3:
#             exit()


print("1:sign up\n")
print("2:sign in\n")
print('3:exit')
x=int(input("Enter 1 or 2\n"))
match x:
    case 1:
        username=input("enter username\n")
        password=input("enter password\n")
        phone=input("enter mobile number")
        with open('login.txt','a') as f:
            f.write('username:'+username+'password:'+password+'phone number:'+phone+'\n')
    case 2:
        username=input("enter username\n")
        password=input("enter password\n")
        with open('login.txt','r') as f:
            out=f.read()
            cred=username+''+password
            if(cred in out):
                print("welcome")
            else:
                print("invalid")

                