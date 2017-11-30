#sets are data structures like dictionaries/lists
#used  when you need uniqueness of elements
a = set() #how to create empty set, {} creates empty dictionaries
num_set = {1,2,3,4,5}
print(2 in num_set)
num_set.add(2) #use add not append
print(num_set) #sets can't have duplicates - makes it faster to check if there is an element
num_set.remove(3) #removes number 3, not index 3
print(num_set)
num_set.pop() #gets rid of first element 
print(num_set)
other_set = {2, 10, 12, 13, 14, 'Apple'}
print(other_set)
print(num_set | other_set) #combines both 
print(num_set & other_set) #only those found in both
print(num_set - other_set) #items in first, not in second
print(other_set - num_set)
print(other_set ^ num_set) #opposite of &, the items in either, not in both
