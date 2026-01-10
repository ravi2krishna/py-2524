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
# employee_info("ravi","ravi@gmail.com") # TypeError: employee_info() missing 1 required positional argument: 'emp_location'

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
    
# With Default Arguments Correct Placement
def employee_info(emp_name,emp_email,emp_location,org_name="Google",emp_mobile="999"): 
     print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")
    
# Arbitrary Positional Arguments
# def add_numbers(a)
# def add_numbers(a,b)
# def add_numbers(a,b,c,d)

# def add_numbers(*a)

def add_numbers(*nums):
    print(nums)

add_numbers(10)
add_numbers(10,20)
add_numbers(10,20,30,40,50)

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

print("=" * 20)

# Without return 
def add(a,b):
    a + b

add(10,20)
print(add(10,20)) # without return default is None

# With return 
def add(a,b):
    return a + b

add(10,20)
print(add(10,20))

# Function Composition 
def sub(c,d,e): # add c + d then minus e 
    return add(c,d) - e

print(sub(3,4,5)) # 2

# return - should be last part of statement to be executed
def add(a,b):
    return a + b
    print("Calculation Done") # Code is structurally unreachable

print(add(100,200))

# multiple return statements, then first will be considered
def math_ops(a,b):
    return a + b
    return a - b # Code is structurally unreachable
    return a * b # Code is structurally unreachable
    return a / b # Code is structurally unreachable

# multiple return statements
def math_ops(a,b,opr):
    if opr == "+":
        return a + b
    elif opr == "-":
        return a - b
    else:
        return "Invalid Operator"

print(math_ops(20,10,"+"))
print(math_ops(20,10,"-"))
print(math_ops(20,10,"^"))

# Local Scope
def add():
    la = 10 # local variable
    lb = 20 # local variable
    print(la) # accessed within function
    print(lb) # accessed within function
    
add()

# print(la) # accessed local outside function # NameError: name 'la' is not defined. Did you mean: 'a'?

# Local Scope
def add(la,lb): # la & lb are local variable
    print(la) # accessed within function
    print(lb) # accessed within function

add(30,40)

# print(la) # accessed local outside function # NameError: name 'la' is not defined. Did you mean: 'a'?

# Global Scope
ga = 100 # global variable 

def add(la,lb): # la & lb are local variable
    print(la) # accessed within function
    print(lb) # accessed within function
    print(ga) # global variable, accessed within function
    
add(50,60)
print(ga) # global variable, accessed outside function

# name conflicts
ga = 100 # global variable 
def add(la,lb,ga): # la & lb are local variable
    print(la) # accessed within function
    print(lb) # accessed within function
    print(ga) # local variable accessed within function, as per preference
    print(globals()['ga']) # global variable accessed within function, using globals()

add(50,60,70)

# Global Variable scenario outside function 
count = 0
print(count)
count += 1
print(count)

# Global Variable scenario inside function 
count = 0
def increment():
    global count
    count += 1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    return count
print(increment())

# Built In Functions 
# id(), type(), dir(), input(), len(), max(), min()
data = [10,20,30,40,50]
print(id(data))
print(type(data))
print(dir(data))
print(len(data))
print(max(data))
print(min(data))
# print(dir(__builtins__)) # checking built in 

# Regular Function i.e without lambda
def add(a,b):
    return a + b 
print(add(10,20))

# With lambda function 
# syntax -> lambda arguments:expression
lambda a,b:a + b 
print((lambda a,b:a + b) (30,40))

# Without lambda
def is_even_num(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even_num(10))
print(is_even_num(5))

# With lambda
# syntax -> lambda arguments:expression
lambda num:num % 2 == 0
print((lambda num:num % 2 == 0)(12))
print((lambda num:num % 2 == 0)(7))

# Without lambda
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")

employee_info(emp_name="Ravi",emp_email="ravi@gmail.com",emp_location="Hyd")

# With lambda
# syntax -> lambda arguments:expression
print((lambda emp_name,emp_email,emp_location:print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")) (emp_name="john",emp_email="john@gmail.com",emp_location="NYC"))

# Without map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5] ==> [1,4,9,16,25]
def square_list(numbers):
    squared_list = []
    for num in numbers:
        squared_list.append(num * num)
    return squared_list

print(square_list([1,2,3,4,5]))

# With map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5] ==> [1,4,9,16,25]
# syntax -> map(function, iterable)
# syntax -> lambda arguments:expression
# lambda num: num * num 
map((lambda num: num * num ), [1,2,3,4,5])
print(map((lambda num: num * num ), [1,2,3,4,5]))
print(list(map((lambda num: num * num ), [1,2,3,4,5])))

# real world use case of map -> find me prices after discounts 
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},
]

# syntax -> map(function, iterable)
# lambda product: product["price"] - product["price"] * product["discount"] / 100
# 80000 -> 80000 - 80000 * 10 / 100 = 72000 
# lambda p: p["price"] - p["price"] * p[]"discount"] / 100
print(list(map((lambda p: p["price"] - p["price"] * p["discount"] / 100), products)))
prices_after_discount = list(map((lambda p: p["price"] - p["price"] * p["discount"] / 100), products))
print("Prices After Discount: ", prices_after_discount)


# without filter()
# Write a script/program to take a list of numbers and return the even list of numbers 
# [1,2,3,4,5,6,7,8,9,10] ==> [2,4,6,8,10]
def even_list(numbers):
    evened_list = []
    for num in numbers:
        if num % 2 == 0:
            evened_list.append(num)
    return evened_list

print(even_list([1,2,3,4,5,6,7,8,9,10]))


# with filter()
# Write a script/program to take a list of numbers and return the even list of numbers 
# [1,2,3,4,5,6,7,8,9,10] ==> [2,4,6,8,10]
# filter(function, iterable)
# lambda num: num % 2 == 0
filter((lambda num: num % 2 == 0), [1,2,3,4,5,6,7,8,9,10])
print(filter((lambda num: num % 2 == 0), [1,2,3,4,5,6,7,8,9,10]))
print(list(filter((lambda num: num % 2 == 0), [1,2,3,4,5,6,7,8,9,10])))

# real world use case of map -> find me premium products i.e costs above 25000
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},
]

print(list(filter((lambda p: p["price"] > 25000), products)))
premium_products = list((filter((lambda p: p["price"] > 25000), products), products))
print("Premium Products: ", premium_products)

# without reduce()
# Write a script/program to take a list of numbers and return the product of all numbers 
# [1,2,3,4,5] ==> [1*2*3*4*5 ==> 120]
def mul_numbers(numbers):
    result = 1
    for num in numbers:
        result = result * num 
    return result
print(mul_numbers([1,2,3,4,5]))

# with reduce()
# Write a script/program to take a list of numbers and return the product of all numbers 
# [1,2,3,4,5] ==> [1*2*3*4*5 ==> 120]
# reduce(function, iterable)
from functools import reduce
print(reduce((lambda result,num: result*num),[1,2,3,4,5]))

# real world use case of map -> find me total cart value of products
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},
]
prices = list(map((lambda p:p["price"]),products))
print(prices)
print(reduce((lambda total_cart_value,price: total_cart_value+price),prices))
total_cart_value = reduce((lambda total_cart_value,price: total_cart_value+price),prices)
print("Total Cart Value: ",total_cart_value)
