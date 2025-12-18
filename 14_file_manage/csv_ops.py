# Working With CSV Files 

import csv

# Read Data 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        print(row)

print("=" * 50)    

# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
filter_by_city = "Delhi"
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row)
        # print(row[3])
        if row[3] == filter_by_city:
            print(row)

print("=" * 50)    

# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from tcs  
filter_by_email = "@tcs.com"
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row)
        # print(row[3])
        if row[1].endswith(filter_by_email):
            print(row)

print("=" * 50)    

# Assume We Have 10K -> 100k Students Records In Sample CSV File 
# Customer Requirement: Fetch me all the students from tcs  
filter_by_email = "@tcs.com"
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row)
        # print(row[3])
        if row[3].endswith(filter_by_email):
            print(row)

print("=" * 50) 

# Assume We Have 10K -> 100k Students Records In Sample CSV File 
# Customer Requirement: Fetch me all the students from tcs  
filter_by_email = "@tcs.com"
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        # print(row)
        if row['email'].endswith(filter_by_email):
            print(row)

print("=" * 50) 

# Assume We Have 10K -> 100k Students Records In Sample CSV File 
# Customer Requirement: Fetch me all the students from tcs  
filter_by_email = "@tcs.com"
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        # print(row)
        if row['email'].endswith(filter_by_email):
            print(row)

print("=" * 50) 
