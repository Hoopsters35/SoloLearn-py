class Rectangle:
	
	def __init__(self, length, width):
		self._length = length
		self._width = width
		
	def calcArea(self):
		return self._length * self._width
		
	@classmethod #decorator to allow the method to be called on the class instead of an instance
	def getSquare(cls, side): #cls tag to show youre using the class not the object
		return cls(side, side) #creates an instance of rectangle based on one parameter
		
square = Rectangle.getSquare(5)
print(square.calcArea())

class Pizza:
	def __init__(self, toppings):
		self.toppings = toppings
		
	@staticmethod #decorator to allow you to call the method on something outside the class without an object
	def checkToppings(topping): #used to make the all statement work
		if topping == 'mushrooms':
			raise ValueError('No mushrooms!')
		else: return True
		
	def makePie(self):
		print("Smells good!")
		
ingredients = ['bacon', 'cheese', 'sausage']
if all(Pizza.checkToppings(i) for i in ingredients): #method called before the object is made
	pizza = Pizza(ingredients)
	
pizza.makePie()