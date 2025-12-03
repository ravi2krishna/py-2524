# Enhanced Student Grade Tracker

print("=" * 50)
print("         Enhanced Student Grade Tracker")
print("=" * 50)

# Validate ID 

student_id_valid = False 

while not student_id_valid:
    student_id = input("Enter ID: ")
    
    # check for partial validation of id -> later you implement complete validation
    if student_id.isdigit():
        student_id = int(student_id)
        if student_id > 0:
            student_id_valid = True
        else:
            print("Non-Zero Values Allowed")
    else:
        print("Only Numeric Values Allowed")

print("Student ID: ",student_id)