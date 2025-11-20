# Requirement

# Create a python application to calculate the fee discount for students
# based on their grade levels and academic Performance
    
student_name = input("Enter Name: ")
student_grade = int(input("Enter Grade: "))
student_fee = int(input("Enter Fee: "))
is_academic_topper = input("Are You Topper? (yes/no) ")

# initial discount
discount = 0

# validation of grade 
if 1 <= student_grade <= 12: 
    print("======= Process Fee Calculation=======")
    
    # discount for 9 to 12
    if student_grade >=9 and student_grade <=12:
        if is_academic_topper == "yes":
            discount = 0.2 # 20% discount as topper
            print("Academic Topper Discount Applied")
        else:
            discount = 0.1 # 10% discount as high school student
            print("High School Discount Applied")
        
    # discount for 6 to 8
    elif student_grade >=6 and student_grade <=8: 
        discount = 0.05 # 5% discount as mid school student
        print("Mid School Discount Applied") 
    else:
        discount = 0
        print("No Discount Applied For Other Grades") 
        
    # Additional Discounts -> use match case
    match student_grade:
        case 10:
            discount += 0.03 
        case 12:
            discount += 0.05 
        case _:
            discount += 0 # do nothing 
            # pass 
        
    # get discount calculation 
    discount_amount = student_fee * discount
    fee_to_pay = student_fee - discount_amount
    
    # Display Results 
    print(f"Student Name: {student_name}")
    print(f"Student Grade: {student_grade}")
    print(f"Actual Fee: {student_fee}")
    print(f"Discount: {discount_amount}")
    print(f"Final Fee: {fee_to_pay}")
    
else:
    print("Invalid Grade Only (1-12) Allowed")