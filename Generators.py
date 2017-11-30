#generators are functions that use the yield statement instead of return
#they become functions that are iterable
#internal variables are not destroyed after the yield line
def countToN(n):
	idx = 1
	while idx <= n:
		yield idx
		
		idx += 1 #this is where the function picks up after being called again in the for loop
		

for i in countToN(7): #prints each number yielded on a line
	print(i)

for i in range(5): #prints a list of the numbers generated for each i in the range
	n = list(countToN(7))
	print(n) 