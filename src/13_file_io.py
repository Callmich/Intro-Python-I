"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
fooReader = open('src/foo.txt', "r")
print(fooReader.read())
fooReader.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
barMaker = open("src/bar.txt", "w")
barMaker.write("I am a bar\n")
barMaker.write("I am a bar also\n")
barMaker.write("A third bar am I")
barMaker.close()

barReader = open('src/bar.txt', "r")
print(barReader.read())
barReader.close()