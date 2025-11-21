# Improvised Voting Application 
# Add Identity Check 
# Check Below approach 
age = int(input("Enter Age: "))
has_id = input("Do You Have ID (yes/no): ")
if age >=18 :
    print("You can Vote")
elif has_id == "yes":
    print("You Can Vote")
else:
    print("You Cannot Vote")

    
# Let's use nested conditionals 
age = int(input("Enter Age: "))
if age >=18:
    has_id = input("Do You Have ID (yes/no): ")
    if has_id == "yes":
        print("You Can Vote")
        # if hierarchy can continue
    else:
        print("You Cannot Vote Without ID")
else:
    print("You Cannot Vote")