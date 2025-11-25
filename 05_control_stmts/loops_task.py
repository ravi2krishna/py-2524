# Simulate ATM Pin Functionality (ATM/OTP/Passwords etc)

actual_otp = 2345

# use built in random module to make it close to real world scenario 
# import random
# actual_otp = random.randint(1000,9999)
# print(f"OTP Generated & Sent To Mobile {actual_otp}")

attempts = 3

# num = "123456"
# print(len(num))

while attempts > 0:
    print(f"You Have {attempts} Attempts Left")
    user_otp = int(input("Enter OTP: "))
    
    if (len(str(user_otp))) != 4:
        print("OTP Must be 4 Digits")
        attempts -= 1
        continue 

    if user_otp == actual_otp:
        print("Correct OTP: Transaction Success")
        break
    else:
        print("InCorrect OTP ")
        attempts -= 1

else:
    print("Max Attempts Reached, Try After 24 Hours")
    