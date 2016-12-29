with open("ex36_1.py","r") as files:
	print files.read()

class FUN:
	def __init__(self, mystring):
		exec("self." + mystring)

f = FUN("age = 11")
print f.age

c = eval('2*3')
print c

globals = {'x':7,'y':10,'names':['aa','bb','cc']}
locals = {}
a = eval("3*x+4*y",globals,locals)
print a

exec("for i in names: print i",globals,locals)

 
