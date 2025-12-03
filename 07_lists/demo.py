# Working With Lists 

# empty list 
empty_list = []
print(empty_list)
print(type(empty_list))

# empty list 
empty_list = list()
print(empty_list)
print(type(empty_list))

# list with numeric data 
data = [10,20,30,40,50]
print(data)

data = list([10,20,30,40,50])
print(data)

# list with texts data 
data = ["python","django","ai"]
print(data)

# list with mixed data 
data = [10,20,30,"python","django","ai",3.5,True]
print(data)

# Accessing Data 
data = [10,20,30,40,50]
print(data)

first_element = data[0]
last_element = data[-1]

print(first_element)
print(last_element)

# print(data[10]) # IndexError: list index out of range

# Access Range Of Data/Values
data = [10,20,30,40,50]
print(data)
print(data[1:3:1]) # 20,30
print(data[0:5:2]) # 10,30,50

# Access Individual Elements -> 10k elements -> below is not efficient 
data = [10,20,30,40,50]
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])

# Access Individual Elements -> 10k elements -> below is efficient 
data = [10,20,30,40,50]
for num in data:
    print(num)
    # print(num,end=" ")

# Apply Operators -> Multiply each element by 10 times and give result
data = [10,20,30,40,50]
for num in data:
    print(num * 10)
    
# Apply Conditionals -> Give me only even values 
data = [10,20,35,45,50]
for num in data:
    if num % 2 == 0:
        print(num)

# Perform transformations -> Give me in Upper Case
data = ["python","django","ai","ai"]
for course in data:
    print(course.upper())

# Duplicates -> Allowed 
data = [10,20,30,10,40,50,10]
for num in data:
    print(num)
    
# List Operations 
print(dir(data))