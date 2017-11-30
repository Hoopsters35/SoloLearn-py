from Cat import * #inherits cat while inherits animal
from ClassStaticMethods import * #from filename import modules
Zoey = Cat('Zoey', 'black and white')
Zoey.speak()
Zoey.walk()
Zoey.superspeak()
print(Zoey.welp) #directly accessed
print(Zoey._owner) #imported like normal
print(Zoey._Cat__furcolor) #finds the variable
#print(Zoey.__furcolor) #gives an error

square = Rectangle.getSquare(4)
print(square.calcArea())