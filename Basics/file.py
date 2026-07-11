name=input("enter: ")
file = open("names.txt","a")
file.write(name,end="\n")
file.close()