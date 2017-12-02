import re

#\1 - \99 will return the group matched at the given position
#
pattern = r"(cat) (dog) \2"
if re.search(pattern, "cat dog dog"): #matches because dog was the second group, and i called for a repitition of the second group
	print("matched 1")
if re.search(pattern, "cat dog"):
	print('matched 2')

#\d refers to a digit (0-9), \s refers to a whitepace (space, \t\n\r\f\v), \w refers to a word character (a-zA-Z0-9_)