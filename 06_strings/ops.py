# String Methods / Operations 

# Simulate Gmail Functionality 
# RAvI2KRishNA -> ravi2krishna@gmail.com 
#         RAvI2KRishNA -> ravi2krishna@gmail.com 

email = input("Enter Your Email ID: ")
format_email = email.lower() # lower
format_email =  format_email.strip() # remove white space
format_email = format_email + "@gmail.com" # concat 
print("Original Email: "+email)
print("Formatted Email: "+format_email)

# Simulate PAN Functionality 
# https://www.pan.utiitsl.com/panonline_ipg/forms/csfPan.html/csfPreForm

pan = input("Enter Your PAN ID: ")
# print(pan.isalnum())
if pan.isalnum(): # isalnum()
    print("Given PAN: "+pan)
    print("Formatted PAN: "+pan.upper()) # upper()
else:
    print("Invalid PAN ID")

# Simulate Phone ISD Scenario 
# https://us1.discourse-cdn.com/flex016/uploads/weweb/original/2X/d/dbe25afb4aeb05640347e2f7c1b7ae532ebb28f2.png

mobile = input("Enter Phone Number with ISD Code: ")
if mobile.startswith("+1"): # startswith()
    print("Calling US Number - Charged in Dollars")
elif mobile.startswith("+91"):
    print("Calling INDIA Number - Charged in Rupees")
elif mobile.startswith("+33"):
    print("Calling FRANCE Number - Charged in Euros")    
else:
    print("Invalid Number - Only US, INDIA & FRANCE supported")    
    
# Simulate Email Synchronization 
source_email = input("Enter Source Email ID: ")
destination_email = input("Enter Destination Email ID: ")

if source_email.endswith("@gmail.com") and destination_email.endswith("@gmail.com"):
    print("Email Synchronization Started")
else:
    print("Email Synchronization Failed")

# Simulate CSV Data from a file and perform some operations 
# Name,Email,Age,City,Job_Role
emp_data = "Johnny,john@apple.com,45,Hyd,Developer"
# Requirement: Display Employee Name & Job Role 
emp_name = emp_data[0]
emp_role = emp_data[-1]

print("Employee Name: "+emp_name)
print("Employee Role: "+emp_role)

emp_name_sliced = emp_data[0:4]
print("Employee Name: "+emp_name_sliced)

# We can use split for above dynamic extractions 
# split gets the data splitted by space by default 
emp_data_extracted = emp_data.split(",")
print(emp_data)
print(emp_data_extracted)

print("Employee Name: "+emp_data_extracted[0])
print("Employee Role: "+emp_data_extracted[-1])

# Simulate Amazon Order Email Confirmation Template Based System
order_template = "Hello your order with order_id has been shipped"
order_ids = "AMZ-123,AMZ-234,AMZ-345,AMZ-456,AMZ-567"
orders_extracted = order_ids.split(",")
for amz_order_id in orders_extracted:
    user_email = order_template.replace("order_id",amz_order_id)
    print(user_email)
