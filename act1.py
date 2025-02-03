from abc import ABC, abstractmethod
class Abscls(ABC):
    def print(self,x):
        print("value which is passed is: ", x)

    @abstractmethod
    def task(self):
        print("Inside Abstract ")

class testCls(Abscls):
    def task(self):
        print("Inside test class")

obj = testCls()
obj.task()
obj.print(50)