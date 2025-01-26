

user={
    "name":[],
    "password":[]    
}

class Test:
    def __init__(self):
        print("hello welcome")
        while True:
            print("menu ")
            print("1 : signup ")
            print("2 login ")
            ch=input("enter your choice ")
            if ch==1:
                self.signUp()
            else:
                print(user)
                self.login()

    def signUp(self):
        self.name=input("enter signup ")
        self.password=input("enter password ")
        user["name"].append(self.name)
        user["password"].append(self.password)

    def login(self):
        self.name=input("enter name ")
        self.password=input(" enter password ")
        if user["name"]==self.name and user["password"]==self.password:
            print(" Wow user login successfull ")
        else:
            print("failed to login ")


user1=Test()