# Variables 

# Assign Data (Store Data)
student_name = "Ravi" # string data 
student_age = 20 # int data 
student_gpa = 9.5 # float data 
student_passed = True # boolean data 
student_aadhar = None # no data 

# Retrieve Data (Get Data) -> use print()
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)
print(student_aadhar)

# Retrieve Data (Get Data) -> use print()
print("Student Name is: student_name")
print("Student Name is: " +student_name)
# print("Student Age is: " +student_age) # TypeError: can only concatenate str (not "int") to str
print("Student Age is: " ,student_age)
print("Student GPA is: " ,student_gpa)
print("Student Passed: " ,student_passed)
print("Student Aadhar ID: " ,student_aadhar) 

# Retrieve Data Identity (Get Memory Address) -> use id()
print(id(student_name))
print(id(student_age))
print(id(student_gpa))
print(id(student_passed))
print(id(student_aadhar))

# Memory Model In Python With Simple Types 
value_x = 10
print(id(value_x))

value_y = 20
print(id(value_y))

value_z = 10
print(id(value_z))

# Memory Model In Python With Complex Types 
value_x = [10,20,30]
print(id(value_x))

value_y = [40,50,60]
print(id(value_y))

value_z = [10,20,30]
print(id(value_z))

# Type Of Data
print(type(student_name))
print(type(student_age))
print(type(student_gpa))
print(type(student_passed))
print(type(student_aadhar))
print(type(value_z))

