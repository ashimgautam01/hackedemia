import pandas as pd

dist={
    "name":[],
    "address":[]
}
n=int(input("enter number of person\n"))

for i in range(1,n+1):
    name=input("enter your name\n")
    add=input("enter your address\n")
    dist["name"].append(name)
    dist["address"].append(add)

distf=pd.DataFrame(dist)
distf.to_csv("data.csv",index=False)

display=pd.read_csv("data.csv")
print(display)
print(display[distf["address"]=="pokhara"])