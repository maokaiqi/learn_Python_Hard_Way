print "put your filename:",
txt = raw_input('>')
txtcontent = open(txt)
print txtcontent.read()
txt.close()

