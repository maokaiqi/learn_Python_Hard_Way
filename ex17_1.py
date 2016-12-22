from sys import argv
from os.path import exists

script, fromfile, tofile = argv

print exists(tofile)
a = open(fromfile)

con = a.read()
print len(con)
b = open(tofile,'w')
con1 = b.write(con)

a.close()
b.close()

