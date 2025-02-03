#cats and dogs

class Cat:
    def __init__(self,name):
        self.name = name
        

    def make_sound(self):
        print("I am cat. My name is ",self.name)
        print("Meow Meow")


class Dog:
    def __init__(self, name):
        self.name = name
        

    def make_sound(self):
        print("I am dog. My name is ",self.name)
        print("Bark ")


cat1 = Cat("kitty")
dog1 = Dog("doggy")

for animal in (cat1, dog1):
    animal.make_sound()

  
