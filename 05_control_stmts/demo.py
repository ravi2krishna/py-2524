# Control Structures

# Indentation
print("Hello")

#  print("Hello") # IndentationError: unexpected indent 

# if condition 
# if 5 > 2:  # IndentationError: expected an indented block after 'if' statement on line 9
# print("yes 5>2 that is correct")

# if condition 
if 5 > 2:  
 print("yes 5>2 that is correct") # one space is valid  
                     
if 5 > 2:  
    print("yes 5>2 that is correct") # four spaces is valid and recommended
#  print("i want this line to be executed") # IndentationError: unindent does not match any outer indentation level
    print("i want this line to be executed")

if 4 < 2:
    print("yes 4<2 that is correct")

num = 10
if num > 0:
    print("given number is positive")
if num < 0:
    print("given number is negative")

# if else condition 
num = -10 # assignment 
if num > 0:
    print("given number is positive")
if num == 0: # comparison
    print("given number is zero")
else: 
    print("given number is negative")
    
# input() -> function that reads input from user 
name = input("Enter Your Name: ")
print(name)
print(type(name))

# Interpolation - "f-strings"
print("Welcome: name") # no Interpolation
print("Welcome: {name}") # with Interpolation
print(f"Welcome: {name}") # with Interpolation

# Not to do this 
num1 = input("Enter Number: ")
num1 = int(num1) # type casting
num2 = int(input("Enter Number: "))
sum = num1 + num2 # string concatenation
print(f"Total Sum is {sum}")

num = int(input("Enter Number: "))
if num > 0:
    print(f"given number {num} is positive")
else: 
    print(f"given number {num} is negative")
    
# Voting App 
age = 22
if age >= 18:
    print("You Can Vote")
else:
    print("You Cannot Vote")
 
# Voting App Dynamic
name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
if age >= 18:
    print(f"{name} You Can Vote") # recommended from python3 onwards 
else:
    print("You Cannot Vote ",name)  # python 2 
    
# invalid way 
# if 5 > 2:

# ternary operator / conditional expression
age = int(input("Enter Your Age: "))
# value_if_true if condition else value_if_false     
status = "You Can Vote" if age >= 18 else "You Cannot Vote"
print(status)
