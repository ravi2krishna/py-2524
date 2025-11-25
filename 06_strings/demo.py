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