from Animal import *
class Cat(Animal): #uses __init__ from animal
			
	def speak(self): #overrides the method from animal
		print('Meow')
		
	def superspeak(self):
		super().speak() #how to access the super class method despite overriding it
		
	__furcolor = "clear"
	_owner = 'Justin'
	welp = 'werd'
		
