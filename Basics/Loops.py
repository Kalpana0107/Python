for el in range(0,6,1):
    print(el,end = " ")

list =["hello" , "World","Hello", "User"]

for val in list:
    print(val , end=" ")

while(True):
    x=int(input("Enter here number: "))
    print(x)
    ask = input("do you want to continue: Y or N : ")
    if(ask == 'N'):
        break
    else: continue

House = [
    {'name': 'Harry Potter' , 'house' : 'Gryffindor' ,' Mascot': 'Lion'},
    {'name': 'Draco' , 'house': 'Slytherin','Mascot': 'Snake'}
]
for _ in House:
    print(_)