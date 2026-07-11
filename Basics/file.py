name=input("enter: ")
file = open("names.txt","a")
file.write(name)
file.close()