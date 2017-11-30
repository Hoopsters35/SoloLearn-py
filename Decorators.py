#decorators modify functions and return a new version of that functions
def sayHi():
	print("Hello World!")
	
def decor(func):
	def wrap(): # will end up replacing func
		print('==========')
		func()
		print('==========')
	return wrap #return from the parent function
	
decoratedHello = decor(sayHi) #creates variable that runs the specified higher order function
decoratedHello()

sayHi = decor(sayHi) #overrides the old func with the decorated version
#or
@decor #this automatically applies-  sayHello = decor(sayHello)
def sayHello():
	print('Hi Justin')
	
sayHello()

##==Class decorators==
#@classmethod used to call a method on the class
#@staticmethod used to call a method from a class on something else without an object of the class
