# OOP Basics 

# Class - Blue Print 
# Student -> Real World Entity
class Student:
    # Characteristics / Attributes / Variables 
    student_name = "Ravi"
    student_email = "ravi@gmail.com"

    # statements
    print("Student Name: ",student_name)
    print("Student Email: ",student_email)

print("=" * 50)

# Student -> Real World Entity
class Student:
    # Characteristics / Attributes / Variables 
    student_name = "Ravi"
    student_email = "ravi@gmail.com"

    # Behaviours / Methods 
    def showInfo():
        print("Showing Info")

    # statements
    print("Student Name: ",student_name)
    print("Student Email: ",student_email)

# Object Creation
student_object = Student()
# student_object.showInfo() # TypeError: Student.showInfo() takes 0 positional arguments but 1 was given

print("=" * 50)

# Student -> Real World Entity
class Student:
    # Characteristics / Attributes / Variables 
    student_name = "Ravi"
    student_email = "ravi@gmail.com"

    # Behaviours / Methods 
    def showInfo(self):
        print("Showing Info")

    # statements
    print("Student Name: ",student_name)
    print("Student Email: ",student_email)

# Object Creation
student_object = Student()
student_object.showInfo() # TypeError: Student.showInfo() takes 0 positional arguments but 1 was given

print("=" * 50)

# Student -> Real World Entity
class Student:
    # Characteristics / Attributes / Variables 
    student_name = "Ravi"
    student_email = "ravi@gmail.com"

    # Behaviours / Methods 
    def showInfo(self):
        print("Showing Info")
        print("Student Name: ",self.student_name) # this is recommended style 
        print("Student Email: ",student_object.student_email)

# Object Creation
student_object = Student()
student_object.showInfo() # TypeError: Student.showInfo() takes 0 positional arguments but 1 was given

print("=" * 50)

# Student -> Real World Entity
class Student:
    # Characteristics / Attributes / Variables 
    student_name = "Ravi"
    student_email = "ravi@gmail.com"

    # Behaviours / Methods 
    def showInfo(self):
        print("Showing Info")
        print("Student Name: ",self.student_name) 
        print("Student Email: ",self.student_email)

# Object Creation
student_ravi = Student()
student_ravi.showInfo() 

student_john = Student()
student_john.showInfo() 

student_mike = Student()
student_mike.showInfo() 

print("=" * 50)
    

# Student -> Real World Entity
class Student:
    # special method i.e constructor 
    def __init__(self,student_name,student_email):
        self.student_name = student_name
        self.student_email = student_email

    # Behaviours / Methods 
    def showInfo(self):
        print("Showing Info")
        print("Student Name: ",self.student_name) 
        print("Student Email: ",self.student_email)

# Object Creation
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.showInfo() 

student_john = Student("john","john@gmail.com")
student_john.showInfo() 

student_mike = Student("mike","mike@gmail.com")
student_mike.showInfo() 

print("=" * 50)
    
