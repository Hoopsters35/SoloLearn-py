import re
#created with brackets inside of a raw string
#will return true if any character found inside the brackets is found in the string

pattern1 = r"[aeiou]" #will match if the word contains any letter in the char class
if re.search(pattern1, "grey"): #matches
	print('1Match 1')
if re.search(pattern1, "qwertyuio"): #matches
	print('1Match 2')
if re.search(pattern1, "rhythm"): #no match
	print('1Match 3')