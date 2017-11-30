#lambas are temporary functions
def my_func(f, arg):
	return f(arg)
	
print(my_func(lambda x: 2*x*x, 5))
#lambda keyword  variables used: expresssion
#most often used to get rid of single line functions

def add5(x):
	return x+ 5
	
print(add5(3))

#or
print((lambda x: x+ 5)(3)) #when giving the argument of a lamba in the same line, use parenthesis 
#around both, and dont use a comma