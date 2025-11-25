# Student Grade Tracker

student_id = input("Enter ID: ")
student_name = input("Enter Name: ")
student_attendance = int(input("Enter Attendance: "))

total_score = 0
num_of_subjects = 0

continue_input = "yes"

while continue_input == "yes":
    current_score = int(input(f"Enter Score For Subject {num_of_subjects + 1}: "))
    continue_input = input("Do You Want To Enter Another Score ? (yes/no): ") 
    num_of_subjects += 1
    total_score += current_score

# Average Score 
average_score = total_score / num_of_subjects

# Grade Status 
if average_score >=85:
    print(" Student Secured: A Grade")
elif average_score >=70:
    print("Student Secured: B Grade")
elif average_score >=50:
    print("Student Secured: C Grade")
else:
    print("Student Secured: D Grade")
    
# Attendance Status
attendance_status = "WARNING - LOW ATTENDANCE" if student_attendance < 75 else "OK - GOOD ATTENDANCE"

# Output 
print(f"Student ID: {student_id}")
print(f"Student Name: {student_name}")
print(f"Student Total Score: {total_score}")
print(f"Student Average Score: {average_score}")
print(f"Student Attendance Status: {attendance_status}")

