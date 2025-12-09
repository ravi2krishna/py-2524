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

# Set Specific Operations 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# union(): combine both sets 
print(s1.union(s2))
print(s1 | s2)

# intersection(): common elements from sets 
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)

# intersection_update(): common elements from sets, updates calling set
print(s1.intersection_update(s2))
print(s1)
print(s2)

# difference(): remove common elements from set and give unique elements  
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference(s2))
print(s1 - s2)
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s2.difference(s1))
print(s1)
print(s2)

# difference_update(): same as difference(), but updates calling set 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference_update(s2))
print(s1)
print(s2)

# symmetric_difference(): removes common elements and takes combined elements from both sets 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s1)
print(s2)

# symmetric_difference_update(): same as symmetric_difference(), but updates calling set 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)

# issubset(): checks if given set is subset of another set 
s1 = {10,20,30,40,50}
s2 = {40,50}
s3 = {60,70,80}

print(s1.issubset(s2))
print(s2.issubset(s1))

# issuperset(): checks if given set is superset of another set 
s1 = {10,20,30,40,50}
s2 = {40,50}
s3 = {60,70,80}

print(s1.issuperset(s2))
print(s2.issuperset(s1))

# isdisjoint(): checks if sets have common elements 
print(s1.isdisjoint(s3))
print(s2.isdisjoint(s3))
print(s1.isdisjoint(s2))