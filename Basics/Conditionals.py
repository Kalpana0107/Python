# x=int(input("Enter here number: "))

# # No additional treatment for edge cases
# if(x%2 == 0):
#     print("X is Even.")
# else:
#     print("X is Odd")

# Using try catch
while(True):
    try:
        num= int(input("Enter here a number: "))
        if(num%2 == 0):
            print("X is Even.")
        else:
            print("X is Odd")
        break
        
    except :
        print("Please Enter Valid Input !")
        pass
        