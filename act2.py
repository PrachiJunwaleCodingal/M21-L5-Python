#class animal
from abc import ABC, abstractmethod

class animal(ABC):
	def move(self):
		pass
class human(animal):
	def move(self):
		print("Human can walk and run")
class lion(animal):
	def move(self):
		print("Lion can roar and walk")

prachi = human()
prachi.move()
cub = lion()
cub.move()

