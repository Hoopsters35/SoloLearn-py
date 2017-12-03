import re

#\1 - \99 will return the group matched at the given position
#
pattern = r"(cat) (dog) \2"
if re.search(pattern, "cat dog dog"): #matches because dog was the second group, and i called for a repitition of the second group
	print("matched 1")
if re.search(pattern, "cat dog"):
	print('matched 2')
print()

#\d refers to a digit (0-9), \s refers to a whitepace (space, \t\n\r\f\v), \w refers to a word character (a-zA-Z0-9_)
#capital means opposite
pattern1 = r"\d\s\w"
if re.search(pattern1, "5 h"):
	print("1match 1")
print()

#\A is an anchor to the first position - no text may come before the \A
#\Z is the opposite, nothin g may come after
#\b represents an invisible barrier between \w and \W characters. j;d has 2 \b spaces
pattern2 = r"j\b.\w"
if re.search(pattern2, "dka j;lO"):
	print('2match 1')
print()