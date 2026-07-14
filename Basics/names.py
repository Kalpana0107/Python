import csv
# names=[]

""" with open("names.txt","r") as file:
    for line in file:
        names.append(line.rstrip())

for line in sorted(names):
    print(line)
        
# Use sorted(names,,reverse=True) // prints in reverse sorted z-a

"""

# Remember csv.reader - returns the list
# csv.DictReader - returns a single dictionary
Student =[]

name = input("Enter name: ")
house = input("Enter house name: ")

with open("student.csv","a", newline="") as file:
    writer= csv.writer(file)
    writer.writerow([name,house])

with open("student.csv") as file:
    for line in file:
        row =line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")



""" #either print in this manner (sorted)
def get_name():
    return student["name"]

for student in sorted(Student,key=get_name):
    print(f"{student['name']} is in {student['house']}")

#second way to print (sorted)
for student in sorted(Student, key=lambda student : student["name"]):
    print(f"{student['name']} is in {student['house']}")

#Third way to print (not sorted)
with open("student.csv") as file:
    for line in file:
        row =line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

# Using CSV 
with open("student.csv") as file:
    reader = csv.reader(file)
    for name,house in reader:
        Student.append({"name":name,"house":house})
        
with open("student.csv") as file:
    reader= csv.DictReader()
    for row in reader:
        print(f"{row[0]} is in {row[1]}")


with open("student.csv") as file:
    for line in file:
        name,house=line.rstrip()
        student={"name" : name, "house": house}
        Student.appent(student)

for student in sorted(Student, key=lambda student : student["name"]):
    print(f"{student['name']} is in {student['house']}")  """