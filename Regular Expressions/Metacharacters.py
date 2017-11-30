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
if re.search(pattern2, 'gr0y'): #gr.y is found at exactly the beginning and the end of the expression
	print('2Match 1')
if re.search(pattern2, 'agray'): #gr.y is found at the end, but not the beginning
	print('2Match 2')
if re.search(pattern2, 'graya'): #gr.y is found at the beginning, but not the end
	print('2Match 3')
print()