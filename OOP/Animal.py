class Animal:
	def __init__(self, name, color):
		self.name = name
		self.color = color
		
	def speak(self):
		print('Me speaking')
		
	def walk(self):
		print(self.name + ' is walking')
		
class Dog(Animal): #how to make a new class without importing
	def speak(self):
		print("Ruff!")
		
class Snake(Animal):
	def speak(self):
		print('Sssss')