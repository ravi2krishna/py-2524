# Working With Dictionaries 

# empty dict 
empty_dict = {}
print(empty_dict)
print(type(empty_dict))

# empty dict 
empty_dict = dict()
print(empty_dict)
print(type(empty_dict)) 

# dict with numeric data 
# data = {10,20,30,40,50} # this is set, as there are no keys and only values 
# print(type(data))

# dict with numeric data 
data = {1:10,2:20,3:30,4:40,5:50}
print(type(data))
print(data)

# dict with texts data 
data = {"c1":"python","c2":"django","c3":"ai"}
print(data)

# dict with mixed data 
data = {1:10,2:20,3:30,"c1":"python","c2":"django","c3":"ai","gpa":3.5,"passed":True}
print(data)

# Accessing Data 
data = {1:10,2:20,3:30,4:40,5:50}
print(data)

# Accessing Data for individual elements is done using keys, not index 
# first_element = data[0] # KeyError: 0
# print(first_element)
first_element = data[1]
print(first_element)

data = {"c1":"python","c2":"django","c3":"ai"}
print(data["c2"])

# Access Individual Elements -> 10k elements -> below is not efficient 
data = {1:10,2:20,3:30,4:40,5:50}
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])

# Access Individual Elements -> 10k elements -> below is efficient 
# NOTE - by default we get keys 
data = {1:10,2:20,3:30,4:40,5:50}
for num in data:
    print(num)

for key in data:
    print(key)
    
for key in data:
    print(data[key])

# Apply Operators -> Multiply each element by 10 times and give result
data = {1:10,2:20,3:30,4:40,5:50}
for key in data:
    print(data[key] * 10)    

# Apply Conditionals -> Give me only even values 
data = {1:10,2:20,3:35,4:45,5:50}
for key in data:
    if data[key] % 2 == 0:
        print(data[key])

# Perform transformations -> Give me in Upper Case
data = {"c1":"python","c2":"django","c3":"ai"}
for course in data:
    print(data[course].upper())
    
# Duplicates -> Allowed With Conditions
# Values can be Duplicated
data = {1:10,2:20,3:30,4:40,5:50,6:50,7:10,8:20}
print(data)

# when duplicates keys are given, overridden mechanism is applied 
data = {1:10,2:20,3:30,4:40,5:50,4:50,3:10}
print(data)

# Real World Use Case Of Dictionary is Working with JSON Data Representation 
students = {
    "101": {
        "name": "Ravi",
        "email": "ravi2krishna@gmail.com",
        "courses": ["python","devops","java"],
        "courses_fee": (10000,25000,15000)        
    },
    "102": {
       "name": "John",
        "email": "john@yahoo.com",
        "courses": ["react","node","mongo"],
        "courses_fee": (10000,25000,15000)        
    } 
}

print(type(students))
print(students)
print("=" * 50)
print(students["101"])
# name of 101 
print("Name: ",students["101"]['name'])

# access 2nd course
print("Second Course: ",students["101"]['courses'])
print("Second Course: ",students["101"]['courses'][1])

# access 2nd course price
print("Second Course Price: ",students["101"]['courses_fee'][1])

# based on student email, tell if customer is of google or not 
id = "102"
if students[id]['email'].endswith("@gmail.com"):
    print("Google Customer")
else:
    print("Not Google Customer")

# dict Operations 
print(dir(data))






