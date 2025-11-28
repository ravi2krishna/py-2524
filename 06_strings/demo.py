# Strings 

# define single line strings
s1 = "hello"
print(s1)

s2 = 'hello'
print(s2)

s3 = '''hello''' # not recommended for single line strings
print(s3)

s4 = """hello""" # not recommended for single line strings
print(s4)

# define multi line strings
# define_python = "Python is a high-level, general-purpose programming language. 
#         Its design philosophy emphasizes code readability with the 
#         use of significant indentation. "

define_python = ''' Python is a high-level, general-purpose programming language. 
       Its design philosophy emphasizes code readability with the 
       use of significant indentation.  '''

print(define_python)

define_python = """ Python is a high-level, general-purpose programming language. 
       Its design philosophy emphasizes code readability with the 
       use of significant indentation.  """

print(define_python)

# need single quote in a string -> use double quotes 
question = "How Are You ?"
# answer = 'i'm fine'
answer = "i'm fine"
print(answer)


# need double quote in a string -> use single quotes 
question = "How Are You ?"
# answer = "i"m fine"
answer = 'i"m fine'
print(answer)

# need double & singe quotes in a string -> use triple quotes 
question = "How Are You ?"
# answer = "i"m fine"
answer = ''' i"m fine i'm fine '''
answer = """ i"m fine i'm fine """
print(answer)

# Accessing Strings 
text = "python"
print(text)

# Accessing Characters In Strings Using Index
# Positive Indexing
print(text[0])
print(text[1])

# Negative Indexing
print(text[-1])
print(text[-2])

# Going Beyond Index Range 
# print(text[10]) # IndexError: string index out of range

# Access all characters 
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

# Access all characters 
text = "python"
for char in text:
       print(char)

# len() -> used to check length of string 
print("Length Of String: ",len(text))

# slicing -> string[start:end:step]
text = "python"
print(text[::]) # all optional 
print(text[0:3:1]) # pyt 
print(text[1:3]) # yt 
print(text[0:5:2]) # pto

#             0  1  2  3  4  5 [ Positive Indexing ]
#             p  y  t  h  o  n 
#            -6  -5 -4 -3 -2 -1  [ Negative Indexing ]

print(text[-4:-1:1]) # tho 
print(text[-4:-1:-1]) # empty   
print(text[-4:-6:-1]) # ty   

# String Concatenation 
g = "good"
m = "morning"
print(g+m)

# Formatted String Literals (f-strings)
age = 30
# print("My Age is "+age) # TypeError: can only concatenate str (not "int") to str
print(f"My Age is {age}")

# String Repetition 
laugh = "Hahaha"
print(laugh)

hard_laugh = laugh * 10
print(hard_laugh)

# String Immutability
greet = "hello" # transform to Hello 
print(greet)
print(greet[0])
# greet[0] = "H" # TypeError: 'str' object does not support item assignment
print(greet)

# But above can be achieved using Mutable Objects like List Object 
greet = ['h','e','l','l','o']
print(greet)
print(greet[0])
greet[0] = "H" 
print(greet[0])
