# Protected 

class A:
    def __init__(self,a,b):
        self._a = a # protected
        self._b = b # protected

obj = A(10,20)

# print(obj.a) # Not Accessible 
# print(obj.b) # Not  Accessible 

class B(A):
    def showA(self):
        a = A(30,40)
        print(a._a)

obj = B(10,20)
obj.showA()
