import re

email = input("enter here mail id: ")

if re.search(r"^\w+@\w+\.com$",email):
    print("Valid")
    
else:
    print("Invalid")