# a = open("ex15_sample.txt","w")
# a.write("""This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.""")
#conding:utf-8
#从系统导入argv参数变量模组modules
from sys import argv
#解包unpack argv，将每个参数依次赋予一个左边变量名script 和 filename
script, filename = argv
#打开filename 并赋予左边的变量名 txt
txt = open(filename)
#打印 filename
print "Here's your file %r:" % filename
#读取文件的内容并打印出来
print txt.read()
txt.close()
#再来一遍
print "Type the filename again:"
#输入刚才模组里的filename,赋予给左边的变量名 file_again
file_again = raw_input(">")
#打开这个文件open()，并赋予左边的变量名 txt_again
txt_again = open(file_again)
#读取文件的内容read() 并打印出来
print txt_again.read()
txt_again.close()
