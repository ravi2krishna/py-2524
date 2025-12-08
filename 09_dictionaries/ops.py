# Dictionary Methods/Operations (Mutable) 

data = {"a":"apple","b":"banana"}
print(type(data))

# update(): add / update item
data = {"a":"apple","b":"banana"}
print(data)
data.update({"c":"cherry"}) # if key is not present, then add 
print(data)

data.update({"a":"apricot"}) # if key is present, then update 
print(data)

# pop(): remove an item by key 
data = {"a":"apple","b":"banana"}
print(data)
data.pop("a")
print(data)
# data.pop("c") # KeyError: 'c'
print(data)

# popitem(): remove last item
data = {"a":"apple","b":"banana"}
print(data)
data.popitem()
print(data)

# clear(): remove all items, empty dict 
data = {"a":"apple","b":"banana"}
print(data)
data.clear()
print(data)

# get(): used to get a value for a key 
data = {"a":"apple","b":"banana"}
print(data)
print(data.get("a"))
print(data.get("c")) # no error when key doesn't exist 

# keys(): used to get keys 
data = {"a":"apple","b":"banana"}
print(data)
print(data.keys())
for key in data.keys():
    print(key)
    

# values(): used to get values 
data = {"a":"apple","b":"banana"}
print(data)
print(data.values())
for value in data.values():
    print(value)    
    

# items(): used to get both keys & values 
data = {"a":"apple","b":"banana"}
print(data)
print(data.items())
for item in data.items():
    print(item)
    print(item[0])
    print(item[1])
    
# copy(): create a copy of dict 
data = {"a":"apple","b":"banana"}
print(data)
dict_backup = data.copy()
print(dict_backup)

# setdefault(): returns a value of key if key is already present,
#               if key is not present, then adds/updates item and returns values
data = {"a":"apple","b":"banana"}
print(data)
out = data.setdefault("b","blueberry")
print(data)
print(out)

data = {"a":"apple","b":"banana"}
print(data)
out = data.setdefault("c","cherry")
print(data)
print(out)