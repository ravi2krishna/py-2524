# Working With JSON Data / Files

student = {
    "id": 101,
    "name": "Ravi",
    "email": "ravi2krishna@gmail.com",
    "courses":["python","django","react"],
    "gpa": 9.5
}

print(type(student))
print(student)

# Write Data to JSON File 
import json
with open("14_file_manage/student.json","w") as file_data:
    # json.dump(file_data)# TypeError: dump() missing 1 required positional argument: 'fp'
    json.dump(student,file_data)

# Write Data to JSON File With Indentation
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data,indent=4)

print("=" * 50)

# Read Data from JSON File
with open("14_file_manage/student.json","r") as file_data:
    json_reader = json.load(file_data)
    print(json_reader)
    print(type(json_reader))

# Requirement: Get Student Name & Number Of Courses he joined from student.json 
with open("14_file_manage/student.json","r") as file_data:
    json_reader = json.load(file_data)
print("Student Name: ",json_reader["name"])    
print("Number Of Courses: ",json_reader["courses"])    
print("Number Of Courses In Number: ",len(json_reader["courses"])) 

# Requirement: Check If Student Passed Or Not, based on GPA above 7
with open("14_file_manage/student.json","r") as file_data:
    json_reader = json.load(file_data)
    
if json_reader["gpa"] > 7:
    print(f"{json_reader["name"]} Passed")
else:
    print(f"{json_reader["name"]} Failed")
 
# File Based (dump & load)

# Object Based (dumps & loads)
student = {
    "id": 101,
    "name": "Ravi",
    "email": "ravi2krishna@gmail.com",
    "courses":["python","django","react"],
    "gpa": 9.5
}
    
json_data = json.dumps(student)
print(json_data)
print(type(json_data))

string_data = '{"id": 101, "name": "Ravi", "email": "ravi2krishna@gmail.com", "courses": ["python", "django", "react"], "gpa": 9.5}'
print(type(string_data))
dict_data = json.loads(string_data)
print(dict_data)
print(type(dict_data))

# Building Full Stack Python Application(API) - JSON Use Case 
import urllib.request

url = "https://dummyjson.com/users"

response = urllib.request.urlopen(url)
print(response)

# Read Content
api_data = response.read()
print(api_data)
print(type(api_data))

# Convert Data 
api_data = json.loads(api_data)
print(api_data)
print(type(api_data))

# Customer Requirement: List me Users 
users = api_data['users']
print(users)

# Customer Requirement: List me Users usernames & count of users  
# users = api_data['users']
for user in users:
    print(user['username'])
print("NUmber Of Users: ", len(users))

# Customer Requirement: List me Users with age below 30
for user in users:
    if user['age'] < 30:
        print(user['username'], user['age'])

