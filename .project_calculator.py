class Calculator(object):
    "calculator"


    def __init__(self,a,b):
        "initialize values"
        #attributes
        self.argv1=a
        self.argv2=b


    def add(self):
        "addition a+b=result -> return result"
        return self.argv1+self.argv2


    def divide(self):
        "divide a/b=result -> return result"
        return self.argv1/self.argv2


    def division(self):
        "division a-b=result -> return result"
        return self.argv1-self.argv2

    def multiply(self):
        "multiplying a*b=result -> return result"
        return self.argv1*self.argv2

v1=10
v2=20
c1=Calculator(v1,v2)
print(c1.add())
print(c1.multiply())
print(c1.division())
print(c1.divide())

