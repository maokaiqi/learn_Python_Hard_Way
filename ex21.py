def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just funcions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age:%d,Height:%d,Weight:%d,IQ:%d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height,multiply(weight,divide(iq,2))))

print "That becomes:", what,"Can you do it by hand?"

iq2 = divide(iq, 2)
weight2 = multiply(weight,iq2)
height2 = subtract(height,weight2)
what2 = add(age,height2)

print "That bacomes:", what2,"Can you do it by hand?"
