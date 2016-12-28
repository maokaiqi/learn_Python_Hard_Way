

def listnum(large,addi):
	i = 0
	numbers = []
	while i < large:
		print "At the top i is %d" % i
		numbers.append(i)
		i = i + addi
		print "Numbers now:",numbers
		print "At the bottom i is %d" % i
	print "The numbers:"

	for num in numbers:
		print num

listnum(16,2)

def fornum(large):
	numbers = []
	for i in range(0,large):
		print "At the top i is %d" % i
		numbers.append(i)
		print "Numbers now:",numbers
		
	print "The numbers:"
	for num in numbers:
		print num

fornum(16)

