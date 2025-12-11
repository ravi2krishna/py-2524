# Functional Style Programming 

# Without Functions 

a = 10
b = 5 

# Math Operations 
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print("=" * 10)

a = 20
b = 5 

# Math Operations - Repeated
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print("=" * 10)

a = 100
b = 50

# Math Operations - Repeated
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print("=" * 10)

print("With Functions")

# With Functions 
def math_ops():
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b) 
a = 10
b = 5 
math_ops()
a = 20
b = 5 
math_ops()
a = 100
b = 50
math_ops()

print("=" * 10)

# math_ops(100,200) # TypeError: math_ops() takes 0 positional arguments but 2 were given

# Using Parameters With Functions 
def math_ops(a,b): # a & b are Parameters 
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b) 

# math_ops() # TypeError: math_ops() missing 2 required positional arguments: 'a' and 'b'
math_ops(10,5) # 10 & 5 are Arguments 
math_ops(20,5)
math_ops(100,50)
# math_ops(100,200,300)


# Positional Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")

employee_info("hyderabad","ravi","ravi@gmail.com")
employee_info("ravi","ravi@gmail.com","hyderabad")

# Keywords Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")

employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com")

# No Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name):
    print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")
    
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com",org_name="Google")
employee_info(emp_location="pune",emp_name="john",emp_email="john@gmail.com",org_name="Google")
employee_info(emp_location="bangalore",emp_name="mike",emp_email="mike@gmail.com",org_name="Google")

# With Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name="Google"):
    print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")
    
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com")
employee_info(emp_location="pune",emp_name="john",emp_email="john@gmail.com")
employee_info(emp_location="bangalore",emp_name="mike",emp_email="mike@gmail.com")
employee_info(emp_location="chennai",emp_name="krishna",emp_email="krishna@gmail.com",org_name="META")

# With Default Arguments With Wrong Placement
# def employee_info(emp_name,emp_email,emp_location,org_name="Google",emp_mobile): # Non-default argument follows default argumentPylance
#     print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")

def employee_info(emp_name,emp_email,emp_location,emp_mobile,org_name="Google",org_gst="90291021092"): # Non-default argument follows default argumentPylance
    print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")
    
# Arbitrary Positional Arguments
# def add_numbers(a)
# def add_numbers(a,b)
# def add_numbers(a,b,c,d)

def add_numbers(*nums):
    total = 0
    for num in nums:
        total = total + num 
    print(f"Total Sum: {total}")

add_numbers(10)
add_numbers(10,20)
add_numbers(10,20,30,40,50)

# Arbitrary Keywords Arguments
def profile(**info):
    print(info)
    
profile(fname="ravi")
profile(fname="ravi",lname="krishna",email="ravi@gmail.com")

def bank_transactions(**trans):
    print(trans)
    total = 0
    for transaction in trans:
        total = total + trans[transaction] 
    print(f"You have done transaction which totals to: {total}")

bank_transactions(jan=1000,feb=3000,mar=5000)