import re

#groups are created using parenthesis to surround a pattern - any metacharacters work inside of a group

pattern1 = r"(sweet) (ho(m)e) (Alabama)?" #grouping allows us to access each inner pattern by adding an arg to the group method

match1 = re.search(pattern1, "sweet home Alabama")
if match1:
	print(match1.group())
	print(match1.group(0)) #does the same thing as no arguments, prints everything that matched
	print(match1.group(1)) #indexing of the signular groups begins at 1
	print(match1.group(2))
	print(match1.group(3)) #prints m, because the nested group gets printed after the parent
	print(match1.group(4))
	print(list(match1.groups())) #returns an iterable of the groups

#named groups are used by putting (?P<group_name>group_attributes) these groups are accessable by both the name, and the index
#
#non-capturing groups are defined by (?:group_attributes) and can not be accessed after the pattern is matched, do not count towards
#numbering of the groups, but still are required to match the pattern