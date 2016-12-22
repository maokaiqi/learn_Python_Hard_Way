# coding:utf-8
#导入参数变量模组
from sys import argv
#赋值给左边的script 和 filename
script, filename = argv
#
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."


raw_input("?")

print "Opening the file..."
#打开文件操作，以可以写入的方式，如果没有这个文件会新建一个,会覆盖已经存在的文件
target = open(filename, 'a')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
