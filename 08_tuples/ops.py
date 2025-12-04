# Tuples are Immutable Lists 
data = [10,20,30,40,50]
print(data)
data[2] = 35
print(data)

data = (10,20,30,40,50)
print(data)
# data[2] = 35 # TypeError: 'tuple' object does not support item assignment
print(data)

# index(): used to get the index position of value
data = (10,20,30,40,50)
print(data)
# print(data.index(0)) # ValueError: 0 is not in list
print(data.index(40))

# count(): count the occurrences 
data = (10,20,10,30,10,40,50,10)
print(data)
print(data.count(10))