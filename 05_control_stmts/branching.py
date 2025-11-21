# Branching Statements 

# loop without break 
for num in range(1,11):
    print(num)
    
# loop with break 
for num in range(1,11):
    if num == 5:
        break # stops the loop when num is 5
    print(num)
    
# loop with continue 
for num in range(1,11):
    if num == 5:
        continue # skips the 5th iteration
    print(num)

# req to perform some "future" operations 
# when the emp salary is above 25000
emp_salary = 20000
if emp_salary > 25000:
    pass # ______________
    
# working on next functionality 
print("Working With Next Scenario")