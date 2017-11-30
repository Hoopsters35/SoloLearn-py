#recursion
def getFactorial(n):
	assert n >= 0, "Number must be positive"
	if n == 0 or n == 1:
		return 1
	return n * getFactorial(n-1)
	
print(getFactorial(5))
#f(5) * f(4) * f(3) * f(2) * f(1) 
#f(1) = 1
#f(2) = f(1) * 2
#f(3) = f(2) * 3
#f(4) = f(3) * 4
#f(5) = f(4) * 5

def getFib(n):
	assert n >= 0, "Enter a positive number"
	if n == 0:
		return 0
	elif n == 1:
		return 1
	return getFib(n-1) + getFib(n-2)
	
for i in range(10):
	print(getFib(i))
print(getFib(5))
#f(5) = f(4) + f(3)
#f(4) = f(3) + f(2)
#f(3) = f(2) + f(1)
#f(2) = f(1) + f(0)
#f(1) = 1
#f(0) = 0
#f(2) = 1
#f(3) = 2
#f(4) = 3
#f(5) = 5