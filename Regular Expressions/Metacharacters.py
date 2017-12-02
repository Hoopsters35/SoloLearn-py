#metacharacters are used to find more complex or general patterns in a string
import re

# a . represents any character
pattern1 = r"gr.y" #r marks the raw string and will not use any escape chars
if re.match(pattern1, "grey"): #true because the . in the raw string can be any character
	print('1Match 1')

if re.match(pattern1, "gray"): #^
	print("1Match 2")

if re.match(pattern1, "blue"): #no logical match
	print("1Match 3")
print()

# ^ at the beginning of a raw string says it should be found at the beginning. $ at the end means it should be found at the end
pattern2 = r"^gr.y$"
#best practice to not use re.match, but instead rely on the metacharacters and search the doc
if re.search(pattern2, 'gr0y'): #gr.y is found at exactly the beginning and the end of the expression
	print('2Match 1')
if re.search(pattern2, 'agray'): #gr.y is found at the end, but not the beginning
	print('2Match 2')
if re.search(pattern2, 'graya'): #gr.y is found at the beginning, but not the end
	print('2Match 3')
print()

#to check for repitition use * (0+), + (1+), or {x, y} (x-y) number of repititions, ? (0 or 1 rep)
#{,} = *, {1,} = +, {0,1} = ?
pattern3 = r"egg(spam)*"
if re.search(pattern3, "egg"): #egg followed by 0 spams
	print("3Match 1")
if re.search(pattern3, "eggspamspam"): #egg followed by 2 spams
	print('3Match 2')
if re.search(pattern3, 'spam'): #doesnt have egg, wont match
	print('3Match 3')
print()

pattern4 = r"egg(spam)+" #egg followed by 1+ spams
if re.search(pattern4, "egg"):
	print('4Match 1')
if re.search(pattern4, 'eggspam'):
	print('4Match 2')
print()

pattern5 = r"^egg(spam){2,4}$" #egg followed by 2-4 spams
if re.search(pattern5, 'eggspam'): #only has 1 spam
	print('5Match 1')
if re.search(pattern5, 'eggspamspam'): #has 2
	print('5Match 2')
if re.search(pattern5, 'eggspamspamspamspamspam'): #has 5
	print('5Match 3')
print()

#? checks if there is 0 or one spams after egg as the entire string
pattern6 = r"^egg(spam)?$"
if re.search(pattern6, "egg"):
	print('6Match 1')
if re.search(pattern6, "eggspam"):
	print('6Match 2')
if re.search(pattern6, "eggspamspam"):
	print('6Match 3')
print()

#| is the bitwise or operator, will take either option - commonly used with groups to find varying whole words
pattern7 = r"gr(e|a)y"
if re.search(pattern7, "grey"):
	print('7Match 1')
if re.search(pattern7, "gray"):
	print("7Match 2")
if re.search(pattern7, "greay"): #won't match because operator only takes one of the possibilities
	print('7Match 3')
print()