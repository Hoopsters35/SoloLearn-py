#tuples are immutable
my_tuple = () #empty tuples require the parenthesis
print(my_tuple)
other_tuple = 'hello', 4, 'no', (0, 1, 2) #tuples are default if no [] () {}
my_tuple = (4, 5, 6, 7) #tuples can be completely reassigned, but not appended to
print(my_tuple)
#can be used as keys in dictionaries, can not be changed, faster than lists
#can be nested
#empty tuples can be used for assertions, or as a false value, or to change later

#can use list slicing on tuples (see lists)