# Looping Statements 

# while loop 
count = 1
while count <=5:
    print("Count: ",count)
    count+=1
    
# You Found a lost phone, trying to break passcode 
# At what attempt you will get it unlocked ?
actual_pin = "4567"
user_given_pin = ""

while user_given_pin != actual_pin:
    user_given_pin = input("Enter Pin: ")

print("Phone Unlocked")

# For Loop with sequences / iterables 
list_numbers = [10,20,30,40,50,60,70,80,90,100]
print(list_numbers)

# list has index which start from zero 0=10, 1=20 and so on
# without for loop 
print(list_numbers[0] * 5)
print(list_numbers[1] * 5)
print(list_numbers[2] * 5)
print(list_numbers[3] * 5)
print(list_numbers[4] * 5)

# with for loop 
for num in list_numbers:
    print(num * 5)

# for with when we know number of Iterations in advance 
print("Hi")

# Say Hi now 10 Times 
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")

for num in range(5):
    print(num)
    
for num in range(1,5):
    print(num)
    
for num in range(0,10,1):
    print(num)
    
for num in range(0,10,2):
    print(num)
    
for num in range(10,1,-1):
    print(num)    
    
# Say Hi now 50 Times 
for num in range(50):
    print("Hi ",num)