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

# Check If Passed or Failed 
marks = int(input("Enter Marks: "))
if marks >= 35:
    print("PASSED")
else:
    print("FAILED")

# elif ladder
# Check Grades A, B, C, D etc 
marks = int(input("Enter Marks: "))
if marks >= 90:
    print("A Grade")
elif marks >= 75: 
    print("B Grade") 
elif marks >= 60: 
    print("C Grade")  
elif marks >= 50: 
    print("D Grade")  
elif marks >= 35: 
    print("E Grade")  
else:
    print("Failed") 
    
# match-case 
choice = int(input('Enter Your Choice: '))
match choice:
    case 1:
        print("Option 1 Selected - Task 1")
        print("Processing Task 1")
        print("Completed Task 1")
    case 2:
        print("Option 2 Selected - Task 2")
        print("Processing Task 2")
        print("Completed Task 2")
    case 3:
        print("Option 3 Selected - Task 3")
        print("Processing Task 3")
        print("Completed Task 3")
    case _:
        print("Unknown Option Selected - Invalid Option Task")
        print("Cannot Process Invalid Option")
        print("Only Select (1-3)")

# math-case 
marks = int(input("Enter Marks: "))

match marks:
    case marks if marks >= 90:
        print("A Grade")
    case marks if marks >= 75:
        print("B Grade")
    case marks if marks >= 60:
        print("C Grade")
    case _:
        print("Failed") 
        
# before match-case i.e no match-case
age = 25

if age == 0 or age == 1 or age == 2 or age == 3 or age == 4:
   category = "Toddler"
elif age == 5 or age == 6 or age == 7 or age == 8 or age == 9 or age == 10 or age == 11 or age == 12:
   category = "Child"
elif age == 13 or age == 14 or age == 15 or age == 16 or age == 17 or age == 18 or age == 19:
   category = "Teenager"
elif age == 20 or age == 21 or age == 22 or age == 23 or age == 24 or age == 25 or age == 26:
   category = "Young Adult"
else:
   category = "Adult"

print(category)

age = 2

# after match-case 
match age:
   case 0 | 1 | 2 | 3 | 4:
       category = "Toddler"
   case 2 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
       category = "Child"
   case 13 | 14 | 15 | 16 | 17 | 18 | 19:
       category = "Teenager"
   case 20 | 21 | 22 | 23 | 24 | 25 | 26:
       category = "Young Adult"
   case _:
       category = "Adult"

print(category) 
