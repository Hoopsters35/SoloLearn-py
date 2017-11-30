#Lists are like arrays/arrayLists
list1 = []
list1.append("5")
list1.insert(0, 4)
print(len(list1))
print(list1.index(4))
list1[1] = 8
list1 += [16, 32]
list1 *= 2
print(list1)
print(4 in list1)

#List Slices
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:4]) #slice takes [a:b)
print(squares[2:8:2]) #third argument is step
print(squares[-1:3:-1]) #-1 == last element. can use negative nums to go from the end
print(squares[-1:3]) #prints empty list because start position is after end pos, and default step is 1
name = 'Justin'
print(name[::-1]) #easy way to reverse list/string. strings can use list slices
print(name[2]) #prints char at index 2
print(name[2:]) #prints from index 2 on
print(name[:3]) #prints until [0,3)

#List Comprehensions
cubes = [i**3 for i in range(5)] #returns the operation for each iterated object
print(cubes)
evens = [i**2 for i in range(10) if i**2 % 2 == 0] #can add full conditional statement to eliminate elements
print(evens)

#useful functions

#all returns true if all items in list are true
#any returns true if any in the list meet the condition
#BOTH USE LIST COMPREHENSIONS to create a new list of boolean values
numbers = [5, 10, 21, 25]
if all([i > 4 for i in numbers]):
	print('all items greater than 4')
if any([i % 3 == 0 for i in numbers]):
	print('at least one number is divisble by 3')

#enumerate returns the index and value while iterating through a list as a tuple
for i in enumerate(numbers, 2): #second arg is starting index (takes negatives)
	print(i)

#HIGHER ORDER FUNCTIONS

#map applies a function to each item in an iterable - often uses lambdas
maps = [3, 5, 7, 8, 9]
afterMap = list(map(lambda x: x+4, maps))
# returns a generic iterable - must change to list
#first arg is the function, 2nd is the iterable
print(afterMap)

#filter takes a predicate(bool func) an iterable and returns the elements that all cases that return true
afterFilter = list(filter(lambda x: not x%2 == 0, maps))
print(afterFilter)
#--can also use list comprehensions for this