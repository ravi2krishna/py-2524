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


# Student -> Real World Entity
# Instance Memebers -> Instance Variable & Instance Method
class Student:

    # Class Variable
    institute_name = "Edify"

    # special method i.e constructor 
    def __init__(self,student_name,student_email):
        # Instance Variable
        # self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email

    # Behaviours / Methods 
    # Instance Method
    def showInfo(self):
        print("Showing Info")
        # Accessing Class Variable
        print("Institute: ",self.institute_name) # this is not recommneded style
        print("Institute: ",Student.institute_name) # this is recommneded style
        print("Student Name: ",self.student_name) 
        print("Student Email: ",self.student_email)
    
    # Class Method
    @classmethod
    def change_institute(cls, new_name):
        cls.institute_name = new_name
        # print(self.student_email) # accessing instance data not allowed in class method

# Object Creation
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.showInfo() 

student_john = Student("john","john@gmail.com")
student_john.showInfo() 

student_mike = Student("mike","mike@gmail.com")
student_mike.showInfo() 

Student.change_institute("Lync")

student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.showInfo() 

student_john = Student("john","john@gmail.com")
student_john.showInfo() 

student_mike = Student("mike","mike@gmail.com")
student_mike.showInfo() 

print("=" * 50)


# Student -> Real World Entity
# Instance Memebers -> Instance Variable & Instance Method
class Student:

    # Class Variable
    institute_name = "Edify"

    # special method i.e constructor 
    def __init__(self,student_name,student_email):
        # Instance Variable
        # self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email

    # Behaviours / Methods 
    # Instance Method
    def showInfo(self):
        print("Showing Info")
        # Accessing Class Variable
        print("Institute: ",self.institute_name) # this is not recommneded style
        print("Institute: ",Student.institute_name) # this is recommneded style
        print("Student Name: ",self.student_name) 
        print("Student Email: ",self.student_email)
    
    # Class Method
    @classmethod
    def change_institute(cls, new_name):
        cls.institute_name = new_name
        # print(self.student_email) # accessing instance data not allowed in class method

    # Static Method 
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email # T & T -> T

# Object Creation
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.showInfo() 

student_john = Student("john","john@gmail.com")
student_john.showInfo() 

student_mike = Student("mike","mike@gmail.com")
student_mike.showInfo() 

Student.change_institute("Lync")

student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.showInfo() 

student_john = Student("john","john@gmail.com")
student_john.showInfo() 

student_mike = Student("mike","mike@gmail.com")
student_mike.showInfo() 

# Validate Email
print(Student.validate_email("ravi"))
print(Student.validate_email("ravi@gmailcom"))
print(Student.validate_email("ravi@gmail.com"))
print("=" * 50)