#itertools
from itertools import *
for i in count(3, 2): #runs an infinite loop starting at the argument, 2nd arg is step
	print(i)
	if i >= 10:
		break
		
spamList = list(repeat('spam', 5)) #returns iterable with arg 2 number of arg 1
print(spamList)

a = []
for i in cycle("abc"): #infinitely cycles through  the input
	a.append(i)
	if len(a) > 20:
		break
		
print(a)

nums = list(accumulate(range(8))) #keeps a running sum of the iterable
print(nums)
nums.append(2)
print(list(takewhile(lambda x: x < 25, nums))) #takes items from the iterable while the items 
#return true from the function, then exits

chaina = range(4)
chainb = range(9, 15)
print(list(chain(chaina, chainb)))
#combines two+ iterables into one

letters = ['a', 'b', 'c']
endLetters = ['x', 'y', 'z']
print(list(product(letters, endLetters))) #creates a list containing tuples of each combination
#of one item from each of the two iterables
print(list(permutations(letters))) #creates a list containing tuples of every rearrangement of
#the iterable
print(list(permutations(letters, 2))) #the second arg is the number of elements in each permutation

