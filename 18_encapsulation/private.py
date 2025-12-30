# Private 

class A:
    def __init__(self,a,b):
        self.__a = a # private 
        self.__b = b # private 

obj = A(10,20)

print(obj.a) # Not Accessible 
print(obj.b) # Not Accessible 

# print(obj._A__a) # name mangling -> # You shouldn’t, but you can if you insist.


class CreditCard:
    def __init__(self,card_number,card_pin):
        self.__card_number = card_number # private 
        self.__card_pin = card_pin # private 