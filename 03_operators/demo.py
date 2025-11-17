# Operators

# Arithmetic Operators
num1 = 10
num2 = 5

print("Sum Of Values: ", num1+num2)
print("Difference Of Values: ", num1-num2)
print("Product Of Values: ", num1*num2)
print("Division Of Values: ", num1/num2)
print("Modulus Of Values: ", num1%num2)

print("Floor Division Of Values: ", num1 // num2)

num1 = 3
num2 = 2

print("Floor Division Of Values: ", num1 // num2)
print("Exponentiation Of Values: ", num1 ** num2) # 3 ^ 2

# Compound Assignment Operators
num = 10
num = num + 5 # long hand form
print(num)

num = 10
num += 5 # short hand form
print(num)

num = 10
num *= 5 # short hand form
print(num)

# Increment - increase a value, used in counters with loops 
count = 1
# count++ not valid in python
count += 1
print(count)

# Decrement - decrease a value, used in counters with loops in reverse direction 
count = 10
# count-- not valid in python
count -= 1
print(count)

# Comparison Operators
num1 = 3
num2 = 2

print(num1 == num2)
print(num1 != num2)
print(num1 < num2)
print(num1 > num2)

print("===============")

# Logical Operators
num1 = 3
num2 = 2
num3 = 1
num4 = 4

print(num1 > num2 and num3 > num4) # T and F -> F
print(num1 > num2 and num3 < num4) # T and T -> T

print(num1 > num2 or num3 > num4) # T or F -> T
print(num1 < num2 or num3 > num4) # F or F -> F

print(num1 > num2)
print(not num1 > num2)

# Membership Operators
data = "python is programming language" 
find_word = "python"
find_word = "java"
status = find_word in data
status = find_word not in data
print("Word Found: ",status)

emps_ids = ["101","102","105","107","110"]
find_emp_id = "103"
status = find_emp_id in emps_ids
print("Employee Found: ",status)

data = 10001
find_1 = 1
# status = find_1 in data
print(status) # TypeError: argument of type 'int' is not iterable

# How do i know if an object is iterable or not ?
print(dir(data)) # look for __iter___
print("===============")
print(dir(find_word))
print("===============")
print(dir(emps_ids))

# Identity Operators 
n1 = 10
n2 = 10 
n3 = 1

print( n1 is n2)
print( n1 is n3)
print( n1 is not n3)

# Bitwise Operators

n1 = 5    # 0000000000000101
n2 = 3    # 0000000000000011
# n1 | n2 # 0000000000000111
# n1 & n2 # 0000000000000001

print(n1 & n2) 
print(n1 | n2) 