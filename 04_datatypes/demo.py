# Data Types 

# Numeric Types 

data = 10
print(type(data))

data = -10
print(type(data))

data = 0
print(type(data))

data = 10.5
print(type(data))

data = -10.5
print(type(data))

# data = 3+i5 # like in math 
# print(type(data))

data = 3 + 5j
print(type(data))

# Text/String Type

data = "good morning"
print(type(data))

# Boolean Type

data = True
print(type(data))
data = False 
# data = false 
print(type(data))

# None Type
data = None 
print(type(data))

# List Type 
data = [10,20,30,40,50]
print(type(data))

# Tuple Type 
data = (10,20,30,40,50)
print(type(data))

# Set Type
data = {10,20,30,40,50}
print(type(data))

# Frozen Set Type
data = frozenset({10,20,30,40,50})
print(type(data))

# Dictionary Type 
data = {"ten":10,"twenty":20,"thirty":30}
print(type(data))

# Custom Data Type 
class Student:
    student_id = 101
    student_name = "Ravi"
    student_gpa = 9.5 

class Trainer:
    trainer_id = 101
    
data = Student() # Object i.e variable of type Student 
print(type(data))

data = Trainer() 
print(type(data))

# Type Conversion 
n1 = 10 
n2 = 5.5
sum = n1 + n2 
print(sum)
print(type(sum))

# Type Casting
final_price =1120.80
print(final_price)
print(type(final_price))

final_price_int = final_price
final_price_int = int(final_price)
print(final_price_int)
print(type(final_price_int))
final_price_str = str(final_price)
print(type(final_price_str))

# Some user in a web page was filling form(text box), which has some rating (strings)
rating = "3"

rating = int(rating)

if rating < 5: # TypeError: '<' not supported between instances of 'str' and 'int'
    print("Customer Not Satisfied")
else:
    print("Customer Satisfied")
    
    


