# Student Management System

# Menu Based System -> In Future once you learn full stack, replace with UI Elements like Buttons 

# System Info - READ ONLY (Tuple)
SYSTEM_INFO = ("Edify Technologies","Student Management System","v1")

# Admin Info - READ ONLY (Tuple)
ADMIN_INFO = ("909088080","admin@edify.com")

# System Info On Startup
print("=" * 50)
print(f"Welcome To: {SYSTEM_INFO[0]}")
print(f"Software Name: {SYSTEM_INFO[1]} - {SYSTEM_INFO[2]}")
print("=" * 50)

# Core Functionalities 
# Add Student 
# Student Data -> id, name, multiple duplicate scores, multiple unique skills 
# Lists, Tuples, Dictionaries, Sets ?? -> 
# id(Dict Key), name(Dict value), multiple duplicate scores(List), multiple unique skills(Sets) 
# id, name, multiple duplicate scores, multiple unique skills 

# https://jsoneditoronline.org/images/news/smart_json_formatting.png

# Dictionary to hold all students data 
students = {}

# Build Menu Based System
while True:
    print("Choose an option: ")
    print("1 - Adding Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Read Student")
    print("5 - Exit Application")
    
    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
        print("Adding Student")
        
        student_id = input("Enter ID: ")
        if student_id in students:
            print("Student Already Exists")
        else:
            name = input("Enter Name: ").title() 
            scores = []
            while True:
                score_input = input("Enter Score or Type done: ")
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0 <= score <=100:
                        scores.append(score)
                    else:
                        print("Invalid Score, Score should be (0-100)")
                else:
                    print("Invalid, Only Digits Allowed")
            
            skills = set()
            while True:
                skill_input = input("Enter Skill or Type done: ")
                if skill_input == "done":
                    break  
                skills.add(skill_input)
            
            # Save above student details to dictionary i.e students = {}
            # id, name, multiple duplicate scores, multiple unique skills 
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            
            print("Student Added")
            print(students)
            
    elif choice == "2":
        print("Updating Student")
        
        student_id = input("Enter ID To Update: ")
        if student_id in students:
            new_name = input("Enter Name: ").title() 
            students[student_id]["name"] = new_name
            print("Student Updated")
        else:
            print("Student ID Doesn't Exist")
        
        print(students)
        
    elif choice == "3":
        print("Deleting Student")
        
        student_id = input("Enter ID To Delete: ")
        if student_id in students:
            students.pop(student_id)
            print("Student Removed")
        else:
            print("Student ID Doesn't Exist")
        print(students)
            
        
    elif choice == "4":
        print("Reading Student")
        # {'102': {'name': 'Mike', 'scores': [80], 'skills': {'java'}}}
        for sid, data in students.items():
            name = data['name']
            scores = data['scores']
            skills = data['skills']
            avg_score = sum(scores) / len(scores)
            high_score = max(scores)
            low_score = min(scores)
            skill_count = len(skills)
            
            print(f"ID: {sid}")
            print(f"Name: {name}")
            print(f"All Scores: {scores}")
            print(f"Average Score: {avg_score}")
            print(f"Highest Score: {high_score}")
            print(f"Lowest Score: {low_score}")
            print(f"All Skills: {skills}")
            print(f"Skills Count: {skill_count}")          
        
    elif choice == "5":
        print("Exit Application")
        print("=" * 50)
        print(f"Call Admin On: {ADMIN_INFO[0]}")
        print(f"Email Admin On: {ADMIN_INFO[1]}")
        print("=" * 50)
        break
    else:
        print("Invalid Option, Please Try with (1-5)")