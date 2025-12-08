# Set Methods / Operations 

# add(): add element to set 
data = {10,20,30,40,50}
print(data)
data.add(60)
print(data)

# update(): add multiple elements to set (iterables)
data = {10,20,30,40,50}
print(data)
data.update([60,70,80])
print(data)

# pop(): Removes random element 
data = {10,20,30,40,50}
print(data)
data.pop()
print(data)

# remove(): Removes element based on value 
data = {10,20,30,40,50}
print(data)
data.remove(20)
print(data)
# data.remove(200) # KeyError: 200
print(data)

# discard(): Removes element based on value, if value doesn't exist, no error 
data = {10,20,30,40,50}
print(data)
data.discard(20)
print(data)
data.discard(200) # No KeyError: 200
print(data)


# clear(): Removes all elements, empties set 
data = {10,20,30,40,50}
print(data)
data.clear()
print(data)

# copy(): Makes a copy 
data = {10,20,30,40,50}
print(data)
backup = data.copy()
print(backup)