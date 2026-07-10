x=int(input("Enter here number: "))

# # No additional treatment for edge cases
if(x%2 == 0):
    print("X is Even.")
else:
    print("X is Odd")

# Using try catch
while(True):
    try:
        num= int(input("Enter here a number: "))
        if(num%2 == 0):
            print("Number is Even.")
        else:
            print("Number is Odd")
        break
        
    except :
        print("Please Enter Valid Input (Integer) !")
        pass

name=input("Enter here your name: ")

# Using if - elif - else
if(name == 'Harry' ):
    print("Gryffindor")
elif(name== 'Draco'):
    print("Slytherin")
else:
    print("Invalid name.")

# Using Match
match name:
    case 'Harry':
        print("Gryffindor")
    case 'Draco':
        print("Slyrtherin")
    case _:
        print("Invalid Input")

