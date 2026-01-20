# Working With CSV Files 

import csv

# Read Data from CSV File
with open("14_file_manage/students.csv","r") as file_data:
    # print(file_data.read())
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

# Write Data to CSV File - Overwrite
with open("14_file_manage/emp.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(["name","email","mobile","address"])
    csv_writer.writerow(['Mahesh', '9969450859', 'Hyderabad', 'mahesh381@tcs.com'])
    csv_writer.writerows([['Mahesh', '9969450859', 'Hyderabad', 'mahesh381@tcs.com'],
                         ['Deepak', 'deepak641@tcs.com', '9369382025', 'Chennai'],
                         ['Ravi', 'ravi186@tcs.com', '9876055200', 'Bangalore'],
                         ['Naveen', 'naveen409@tcs.com', '9806720153', 'Hyderabad']])

# Write Data to CSV File - Append
with open("14_file_manage/test.csv","a") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(["name","email","mobile","address"])
    csv_writer.writerow(['Mahesh', '9969450859', 'Hyderabad', 'mahesh381@tcs.com'])
    csv_writer.writerows([['Mahesh', '9969450859', 'Hyderabad', 'mahesh381@tcs.com'],
                         ['Deepak', 'deepak641@tcs.com', '9369382025', 'Chennai'],
                         ['Ravi', 'ravi186@tcs.com', '9876055200', 'Bangalore'],
                         ['Naveen', 'naveen409@tcs.com', '9806720153', 'Hyderabad']])

# Write Data to CSV File - Overwrite
fieldnames = ['name', 'email', 'mobile', 'address']
with open("14_file_manage/new.csv","w") as file_data:
    # csv_writer = csv.DictWriter(file_data) # TypeError: DictWriter.__init__() missing 1 required positional argument: 'fieldnames'
    csv_writer = csv.DictWriter(file_data,fieldnames)
    csv_writer.writeheader() # uses the fieldnames to write the first row of the CSV file, which serves as the column headers.
    csv_writer.writerow({'name': 'Deepak', 'email': 'deepak641@tcs.com', 'mobile': '9369382025', 'address': 'Chennai'})
    csv_writer.writerow({'name': 'Ramu', 'email': 'ramu661@tcs.com', 'mobile': '9833214959', 'address': 'Bangalore'})
    csv_writer.writerows([{'name': 'Balu', 'email': 'balu275@tcs.com', 'mobile': '9168624926', 'address': 'Mumbai'},
                        {'name': 'Hari', 'email': 'hari478@tcs.com', 'mobile': '9564137451', 'address': 'Jaipur'},
                        {'name': 'Naveen', 'email': 'naveen409@tcs.com', 'mobile': '9806720153', 'address': 'Hyderabad'}])

# Write Data to CSV File - Append
fieldnames = ['name', 'email', 'mobile', 'address']
with open("14_file_manage/demo.csv","a") as file_data:
    # csv_writer = csv.DictWriter(file_data) # TypeError: DictWriter.__init__() missing 1 required positional argument: 'fieldnames'
    csv_writer = csv.DictWriter(file_data,fieldnames)
    csv_writer.writeheader() # uses the fieldnames to write the first row of the CSV file, which serves as the column headers.
    csv_writer.writerow({'name': 'Deepak', 'email': 'deepak641@tcs.com', 'mobile': '9369382025', 'address': 'Chennai'})
    csv_writer.writerow({'name': 'Ramu', 'email': 'ramu661@tcs.com', 'mobile': '9833214959', 'address': 'Bangalore'})
    csv_writer.writerows([{'name': 'Balu', 'email': 'balu275@tcs.com', 'mobile': '9168624926', 'address': 'Mumbai'},
                        {'name': 'Hari', 'email': 'hari478@tcs.com', 'mobile': '9564137451', 'address': 'Jaipur'},
                        {'name': 'Naveen', 'email': 'naveen409@tcs.com', 'mobile': '9806720153', 'address': 'Hyderabad'}])