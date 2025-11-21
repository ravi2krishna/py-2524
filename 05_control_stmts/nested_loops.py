# Generate Math Tables 
# 1 X 1 - 1 X 2 - 1 X 3 - 1 X 4 - 1 X 5
# 2 X 1 - 2 X 2 - 2 X 3 - 2 X 4 - 2 X 5
# 3 X 1 - 3 X 2 - 3 X 3 - 3 X 4 - 3 X 5

# Nested for loop 
for outer in range(1,4):
    print("Outer: ",outer)
    for inner in range(1,6):
        print("Inner: ",inner)
        
# Nested for loop 
# 1 X 1 - 1 X 2 - 1 X 3 - 1 X 4 - 1 X 5
for outer in range(1,4):
    print("==============")
    for inner in range(1,6):
        print(f"{outer} * {inner} =  {outer * inner}")
  
# realm world use case with ecommerce app
colors = ["red","yellow","black"]        
sizes = ["XS","S","M","L","XL","2XL"]

for color in colors:
    for size in sizes:
        print(color,size)
        
    
# Nested While loop 
# 1 X 1 - 1 X 2 - 1 X 3 - 1 X 4 - 1 X 5
outer = 1
while outer<4:
    inner = 1
    while inner < 6:
        print(f"{outer} * {inner} =  {outer * inner}")
        inner += 1
    outer += 1
    