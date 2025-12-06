from abc import ABC, abstractmethod

#creating base class
class animal(ABC):
    def move(self):
        pass

#creating sub class human
class human(animal):
    def move(self):
        print("I can walk and run")

#creating sub class snake
class snake(animal):
    def move(self):
        print("I can crawl")

#creating sub class
class dog(animal):
    def move(self):
        print("I can bark")

#creating sub class
class lion(animal):
    def move(self):
        print("I can roar")

H = human()
H.move()

S = snake()
S.move()

D = dog()
D.move()

L = lion()
L.move()