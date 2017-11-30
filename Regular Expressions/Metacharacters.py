#metacharacters are used to find more complex or general patterns in a string
import re

pattern = r"gr.y" #r marks the raw string and will not use any escape chars
if re.match(pattern, "grey"): #true because the . in the raw string can be any character
	print('Match 1')

if re.match(pattern, "gray"): #^
	print("Match 2")

if re.match(pattern, "blue"): #no logical match
	print("Match 3")
