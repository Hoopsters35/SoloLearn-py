#ImportError an import fails
#IndexError an index is out of bounds
#NameError unknown var used
#SyntaxError code cant be parsed properly
#TypeError function is called iwth inappropriate type
#ValueError function called on value of correct type, wrong value
#ZeroDivisionError

#use try/except blocks -- specific excepts before general
#finally keyword means it will always run -- often used to continue code or close files

#raise + type of exception -- automatically have an exception raised if something happens
#raise NameError("Invalid name!") -- raise the error with a message
#in an except block, you can use raise without arguments as 'printStackTrace()'

#assert 2+2 == 4 -> program keeps running
#assert 1+1 == 3 -> program stops with an AssertionError
#can take second argument as a message if it fails: assert (temp >=0), 'Colder than zero!'
#assertion errors can be handled with try-except blocks as well