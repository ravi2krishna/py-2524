# Sets 

# Working With Sets  

# empty set -> by default when  we use empty {}, then it's a dict 
empty_set = {}
print(empty_set)
print(type(empty_set))

# empty set 
empty_set = set()
print(empty_set)
print(type(empty_set))

# set with numeric data 
data = {10,20,30,40,50}
print(data)

data = set({10,20,30,40,50})
print(data)

# set with texts data 
data = {"python","django","ai"}
print(data)

# set with mixed data 
data = {10,20,30,"python","django","ai",3.5,True}
print(data)

# Accessing Data 
data = {10,20,30,40,50}
print(data)

# first_element = data[0] # TypeError: 'set' object is not subscriptable
# last_element = data[-1] # TypeError: 'set' object is not subscriptable

# Access Individual Elements -> 10k elements -> below is efficient 
data = {10,20,30,40,50}
for num in data:
    print(num)
    
# Apply Operators -> Multiply each element by 10 times and give result
data = {10,20,30,40,50}
for num in data:
    print(num * 10)

# Apply Conditionals -> Give me only even values 
data = {10,20,35,45,50}
for num in data:
    if num % 2 == 0:
        print(num)

# Perform transformations -> Give me in Upper Case
data = {"python","django","ai","ai"}
for course in data:
    print(course.upper())
    
# Duplicates -> Not Allowed 
data = {10,20,30,10,40,50,10}
print(data)
for num in data:
    print(num)
    
# set Operations 
print(dir(data))

# Frozenset 
# data = {10,20,30,10,40,50,10}
data = frozenset({10,20,30,10,40,50,10})
print(type(data))
print(dir(data))

