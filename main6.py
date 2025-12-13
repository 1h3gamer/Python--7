class car:
    def __init__(self,type,speed):
        self.type=type
        self.speed=speed
    def set_age(self,type,speed):
        self.type=type
        self.speed=speed
    def get_age(self):
        return self.type and self.speed
    
    def __Add__(self,predict):
        return car(self.type+predict.type) and car(self.speed+predict.speed)
    def __Gt__(self,predict):
        return self.type>predict.type and self.speed>predict.speed
    def __Lt__(self,predict):
        return self.type<predict.type and self.speed<predict.speed
    def __Str__(self):
        return "Combined speed "+str(self.speed)
    def __str__(self):
        return "Combined type"+str(self.type)
    
Bmw = car(5,12)
print(Bmw.get_age())
print(Bmw.__Add__)
print(Bmw.__Gt__)

Ferrari = car(6,18)
print(Ferrari.get_age())
print(Ferrari.__Add__)
print(Ferrari.__Gt__)

print(Bmw<Ferrari)