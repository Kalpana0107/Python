name=input("enter: ")
""" file = open("names.txt","a")
file.write(name)
file.close() """

# Files without closing(Auto close)/ Use of with
with open("hello.txt","a") as file:
    file.write(f"{name}\n")

# File reading
with open("hello.txt" , "r") as file:
    lines= file.readlines()
    
#   Printing in terminal
# for line  in lines:
#     print("hello,",line.rstrip())
    
# Second way of printing 
with open("hello.txt","r") as file:
    for line in file:
        print("hello," , line.rstrip())


    