# List Methods / Operations 

# append(): adds element to end of the list 
data = [10,20,30,40,50]
print(data)
data.append(60)
print(data)

# data.append(70,80,90) # TypeError: list.append() takes exactly one argument (3 given)
data.append([70,80,90])
print(data)

# extend(): adds iterable to end of the list 
data = [10,20,30,40,50]
print(data)
# data.extend(60) # TypeError: 'int' object is not iterable
data.extend([60,70,80,90])
print(data)


data = [10,20,40,50]
print(data)
data.append(30)
print(data)

# insert(): insert data at specific position (index)
data = [10,20,40,50]
print(data)
# data.insert(30) # TypeError: insert expected 2 arguments, got 1
data.insert(2,30)
print(data)

data.insert(10,60) # if index is given out of range, adds at end of list
print(data)

# pop(): removes an element, by default last element
         # if index is provided removes data based on index 
data = [10,20,30,40,50]
print(data)
data.pop()
print(data)

data.pop(0)
print(data)

# data.pop(10) # IndexError: pop index out of range
print(data)

# remove(): remove element based on value 
data = [10,20,30,40,50]
print(data)
# data.remove(0) # ValueError: list.remove(x): x not in list
data.remove(30)
print(data)

data = [10,20,30,10,40,50,10]
print(data)
data.remove(10)
print(data)

# Requirement is remove all occurrences 
data = [10,20,10,30,10,40,50,10]
print(data)
# for i in data:
#     data.remove(10)
# print(data)
while 10 in data:
    data.remove(10)
print(data)  

# clear(): empties list 
data = [10,20,30,40,50]
print(data)
data.clear()
print(data)

# index(): used to get the index position of value
data = [10,20,30,40,50]
print(data)
# print(data.index(0)) # ValueError: 0 is not in list
print(data.index(40))

# count(): count the occurrences 
data = [10,20,10,30,10,40,50,10]
print(data)
print(data.count(10))

# reverse(): reverses the list 
data = [10,20,30,40,50]
print(data)
data.reverse()
print(data)

# sort(): sorts the list default is ascending order 
data = [10,30,20,50,40]
print(data)
data.sort()
print(data)

data = [10,30,20,50,40]
print(data)
data.sort(reverse=True) # descending order 
print(data)

data = ["a","f","z","l"]
print(data)
data.sort()
print(data)
data.sort(reverse=True) # descending order 
print(data)

data = ["a","f",30,20,"z","l"] 
print(data)
# data.sort() # TypeError: '<' not supported between instances of 'int' and 'str'
print(data)

# copy(): creates a backup copy 
data = [10,20,30,40,50]
print(data)
print(data.copy())