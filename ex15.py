from sys import argv

script,filename = argv
text = open(filename)
print "filename : %s" % filename
print text.read()
