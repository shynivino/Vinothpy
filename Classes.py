class Student:  
   empcount=0  
   def __init__(self, rollno, name):  
      self.rollno = rollno  
      self.name = name
      Student.empcount+=1
   def displayStudent(self):  
      print ("rollno : ", self.rollno,  ", name: ", self.name) 
   @classmethod
   def printemployeecount(cls):
       print (cls.empcount)
   @staticmethod
   def checkeligibility(age):
       print(self.rollno)
       if age >= 18 :
           return ("eligible for voting")
       else:
           return("not eligible")

class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()
# passing the object
flying_test(blu) #calls Parrot fly method
flying_test(peggy) #calls Penguin fly method

emp1 = Student(121, "Ajeet")  
emp2 = Student(122, "Sonoo")  

emp1.displayStudent()  
emp2.displayStudent()
Student.printemployeecount()
print(Student.checkeligibility(18))
