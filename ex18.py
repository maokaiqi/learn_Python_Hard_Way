# coding:utf-8
# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takse no arguments
def print_none():
	print "I got nothing'."


print_two("Zed","Shaw")
print_two_again("Zed","Show")
print_one("First!")
print_none()
#函数定义是以def开始的
#函数名称是以字符或者下划线_开头，以字符或者下划线或者数字自由搭配或者单个组成。
#函数名称定义和执行的时候都是跟着括号。
#括号里可以不需要参数，由函数定义时决定，多个参数以逗号隔开。
#不能使用重复的参数名
#函数定义第一行是以):结尾
#代码块以4个空格缩进
#函数结束后新的代码不要缩进
#使用一个函数是，需要调用函数名称
#执行函数需要()
#参数不定，根据定义的需求决定参数个数，多个参数需要以逗号隔开
#以)结尾
