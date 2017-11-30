#don't run this code

#BEST PRACTICE
with open("FilePath", mode) as f:
	#do something here
	#file will automatically close

try:
	mode = [r, w, a] #read(default), write, append. optional add b after for binary mode (non text files)
	myFile = open("filePath", mode)
	contents = myFile.read() # stores all contents as a string
	numBytes = myFile.read(16) #reads 16 bytes - often one character
	oneLine = myFile.readline #stores one line of file and moves cursor to next line
	allLines = myFile.readlines #stores each line of the file in a list
	
	myFile.write() #-- works like a print function -- can be formatted -- returns number of bytes written
	

except ImportError:
	raise
finally: #guarantees closing the file
	myFile.close()