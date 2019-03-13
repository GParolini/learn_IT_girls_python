from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that hit CTRL-c (^C)."
print "if you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target1.write(line1)
target1.write("\n")
target1.write(line2)
target1.write("\n")
target1.write(line3)
target1.write("\n")

print "And finally, we close it."
target1.close()
