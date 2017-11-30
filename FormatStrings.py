#formatting strings
#works with print, write, etc

#either use a printf format style
print("%-5.5s %6.6d, %7.2f" % ("============", 4, 8493.43243242))
#use % in between the format string and the tuple of arguments
#if you need to use variables in the format string, make that string BEFORE and just pass as arg
#- left allign; num before . is guaranteed space to take up; num after . is max space for strings, max dec nums in floats

#or you can use .format on a strings
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2]) #curly braces with index of 2ndary argument
print(msg)
msg2 = "{x}, {y}".format(x=3, y=4) #if not an index, must define in 2nd arg
print(msg2)

#useful string methods
print(','.join(['hi', 'my', 'name', 'is', 'justin'])) #string used as separator, arg is list of items
print('Hello me'.replace('me', 'world')) #first arg is word to be replaced, 2nd arg is replacing word
print('This is a sentence'.startswith('This')) #prints true, because first word is arg
print('This is a sentence'.endswith('sentence')) #prints true, last word is arg
#.lower() and .upper() change case of string - useful for comparing without case sensitive
print('Hello my name is justin'.split()) #default uses a space to split words into a list of words
print('Hello, my name is, justin'.split(',')) #splits when it sees arg



