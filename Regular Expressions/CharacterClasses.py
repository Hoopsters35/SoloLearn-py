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
print()

#you can use ranges within character classes based on ASCII encoding
pattern2 = r"[a-z]" #or [A-Z], [0-9]
if re.search(pattern2, "Hello World"): #contains lower case letter(s)
	print('2Match 1')
if re.search(pattern2, "HELLO WORLD"): #all caps, wont match
	print('2Match 2')