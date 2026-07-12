names=[]

with open("names.txt","r") as file:
    for line in file:
        names.append(line.rstrip())

for line in sorted(names):
    print(line)
        
# sorted(names,,reverse=True) // prints in reverse sorted z-a