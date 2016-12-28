import ex36_1
def bedroom():
	print "welcome"
	ex36_1.dead("good")

def lunchroom():
	print "wrong way!"
	ex36_1.dead("byebye")

def start():
	print "let's go!"
	
	next = raw_input("> ")
	if next == "left":
		bedroom()
	elif next == "right":
		lunchroom()
	else:		
		ex36_1.dead("you must staying here until police arrivd!")

start()
