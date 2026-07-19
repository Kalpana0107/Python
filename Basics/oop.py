
class Tudent:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name!")
        if house not in ["gryfindor","hufflepuff","ravenclaw","slytherin"]:
            raise ValueError("Invalid House")
    
def get_student():
    name = input("enter here name: ")
    house = input("enter here house: ")
    return Tudent(name,house)

def main():
    student =get_student()
    print(student.name)
    
if __name__=="__main__":
    main()
    
    
    
""" 
class Student:
   def __init__(self,name,house,patronus):
       if not name:
           raise ValueError("Missing name!")
       if house not in ["gryffindor","hufflepuff","ravenclaw","slytherin"]:
           raise ValueError("Invalid house")
       self.name=name
       self.house=house
       self.patronus = patronus
       
   def __str__(self):
        return "hello, Student!"
    
  #User defined function
   def charm(self):
       match self.patronus:
           case 'stag':
               return "✌️"
           case 'Otter':
               return "👍"
           case _:
               return "🎶"



def main():
    student = get_stu()
    print("Expected patronus !")
    #print(student)  # If __str__is not then it would just print address
    print(student.charm())


def get_stu():
    
    name=input("enter name: ")
    house=input("enter house: ")
    patronus=input("patronus: ")
    return Student(name,house,patronus)


    
if __name__== "__main__":
    main()


class Student:
   def __init__(self,name,house):
       self.name=name
       self.house=house

   def __str__(self):
       return "a student"
 """
