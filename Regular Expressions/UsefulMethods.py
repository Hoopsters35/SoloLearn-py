import re
pattern = r"spam" #r marks it as a raw string which don't escape any characters such as \n
str = "eggsspamsausagespam"

if re.match(pattern, "spamspamspam"): #Checks the BEGINNING of the string
	print('match from match')
else: print("No match from match")
print()

if re.match(pattern, "eggsspam"):
	print("match from match at beginning of word")
else: print("match didn't find at beginning of word")
print()

if re.search(pattern, str): #finds the pattern anywhere in the string
	print("match from search")
	print(re.findall(pattern, str)) #returns all instances of the pattern in the arg
else: print("no match from search")
print()

for i in re.finditer(pattern, str): #same as find all, but returns iterator of regular expressions
	print(i.start(), i.group()) #i.start() gets the starting index of the word. i.group() gets the word itself
print()

matched = re.search(pattern, str)
if matched:
	print(matched.group()) #prints the word that was found in the string
	print(matched.start()) #prints the starting index of the word in the string
	print(matched.end()) #prints the starting index of the word in the string plus the length of the string
	print(matched.span()) #returns a tuple of (matched.start(), matched.end())
	print()

#re.sub(pattern, repl, string, max) what to find, what to replace the find with, parent string to search, how max num to replace (default all)
str1 = "My name is Justin. Hi Justin! Go Justin!"
pattern1 = r"Justin"
newstr1 = re.sub(pattern1, "Nathan", str1, 2) #replace the first two instances of pattern1 in str1 with "Nathan"
print(newstr1)