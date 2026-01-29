# Exception Handling 

# When No Error -> Nothing To Handle 

print("Program Execution Started")
num1 = 10
num2 = 5
print(num1/num2)
print("Program Execution Completed")

print("=" * 50)

# When there is Error -> Python Handles by stopping the program
print("Program Execution Started")
num1 = 10
num2 = 0
# print(num1/num2) # ZeroDivisionError: division by zero
print("Program Execution Completed")

print("=" * 50)

# When there is Error -> User Handles by try & except, with meaningful info 
print("Program Execution Started")
num1 = 10
num2 = 0
# print(num1/num2) # ZeroDivisionError: division by zero
try:
    print(num1/num2)
except:
    print("OOPS! We Got an Error - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
print("Program Execution Completed")

print("=" * 50)

# When there is No Error -> User Handles by try & except, with meaningful info 
print("Program Execution Started")
num1 = 10
num2 = 5
# print(num1/num2) # ZeroDivisionError: division by zero
try:
    print(num1/num2)
except:
    print("OOPS! We Got an Error - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
print("Program Execution Completed")

print("=" * 50)

# When we have multiple errors 
print("Program Execution Started")
# data = [1,2,'python',0,5]
# data = [1,2,0,5]
data = [1,2,5]
for num in data:
    print(1/num)
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
print("Program Execution Completed")

print("=" * 50)

# When we have multiple errors 
print("Program Execution Started")
data = [1,2,'python',0,5]
for num in data:
    try:
        print(1/num)
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    except:
        print("OOPS! Something Went Wrong")
print("Program Execution Completed")

print("=" * 50)

# When we have multiple errors 
print("Program Execution Started")
data = [1,2,'python',0,5]
for num in data:
    try:
        print(1/num)
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    # IndexError: index out of range
    except TypeError:
        print("OOPS! Dividing String With Number is not supported")
    except ZeroDivisionError:
        print("OOPS! You Cannot Divide Number By Zero")
print("Program Execution Completed")

print("=" * 50)

# When there is No Error -> User Handles by try & except, with meaningful info 
print("Program Execution Started")
num1 = 10
num2 = 5
try:
    print(num1/num2)
except:
    print("OOPS! We Got an Error - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Was Successful")
print("Program Execution Completed")

print("=" * 50)

# When there is No Error -> User Handles by try & except, with meaningful info 
print("Program Execution Started")
num1 = 10
num2 = 0
try:
    print(num1/num2) # Login Success 
except:
    print("OOPS! We Got an Error - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Was Successful") # Then Only Check For OTP
print("Program Execution Completed")

print("=" * 50)

# When there is No Error -> User Handles by try & except, with meaningful info 
# finally - run this for sure
print("Program Execution Started")
num1 = 10
num2 = 0
try:
    print(num1/num2) # Login Success 
except:
    print("OOPS! We Got an Error - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Was Successful") # Then Only Check For OTP
finally:
    print("Program Execution Completed")

print("=" * 50)

# Create Custom Exception 
class MyError(Exception):
    pass 

# Voting App
age = int(input("Enter Age: "))
if age < 18:
    print("You Cannot Vote")
else:
    print("You Can Vote")
    
# Custom Age Exception 
class AgeError(Exception):
    pass 

# Voting App 
age = int(input("Enter Age: "))
if age < 18:
    raise AgeError
else:
    print("You Can Vote")
    
# With Message 
age = int(input("Enter Age: "))
if age < 18:
    raise AgeError("Your Age Must be at least 18 years to vote")
else:
    print("You Can Vote")
    
# Custom ID Exception 
class IDError(Exception):
    pass 

age = int(input("Enter Age: "))
if age < 18:
    raise AgeError("Your Age Must be at least 18 years to vote")
else:
    has_id = input("Do You Have ID? (yes/no) ")
    if has_id != "yes":
        raise IDError("You Must Have ID To Enter")
print("You Can Vote")

# Handle Above Exceptions Now 
age = int(input("Enter Age: "))
try:
    if age < 18:
        raise AgeError("Your Age Must be at least 18 years to vote")
    else:
        has_id = input("Do You Have ID? (yes/no) ")
        if has_id != "yes":
            raise IDError("You Must Have ID To Enter")
except AgeError:
    print("You are not 18 Yet")
except IDError:
    print("Carrying ID is mandatory")
else:
    print("You Can Vote")