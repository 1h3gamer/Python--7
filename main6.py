class Animal:
    def __init__(self,age):
        self.age=age
    def set_age(self,age):
        self.age=age
    def get_age(self):
        return self.age
    
    def __Add__(self,predict):
        return Animal(self.age+predict.age)
    def __Gt__(self,predict):
        return self.age>predict.age
    def __Lt__(self,predict):
        return self.age<predict.age
    def __Str__(self):
        return "Combined age "+str(self.age)
    
c1 = Animal(5)
print(c1.get_age())

c2 = Animal(6)
print(c2.get_age())

print(c1<c2)