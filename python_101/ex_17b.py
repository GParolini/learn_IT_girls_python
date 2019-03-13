from sys import argv
from os.path import exists
script, from_file, to_file = argv
in_file = open(from_file, 'r')
out_file = open(to_file, 'w')

print "Copying from %s to %s" %(from_file, to_file)

out_file.write(in_file.read())
