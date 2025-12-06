from abc import ABC, abstractmethod

#create a base class
class Absclass(ABC):
    def print(self,x):
        print("passed value: ",x)
    @abstractmethod
    def task(self):
        print("We are in the Absclass task")

#create a sub class
class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")

test_obj=test_class()
test_obj.task()
test_obj.print(100)