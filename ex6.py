# coding:utf-8
#格式化 10
x = "There are %d types of people." % 10
#定义变量
binary = "binary"
do_not = "don't"
# 格式化与变量 两个及以上 用括号包裹，逗号隔开
y = "Those who know %s and those who %s." % (binary, do_not)

#打印
print x

print y
#用%r会把引号输出，而%s不会
print "I said: %r." % x
#所以需要再加上引号，双引号里面就需要用单引号；
print "I also said: '%s'." % y

hilarious = False

joke_evaluation = "Isn't that joke so funny?! %r"
#打印 上面两句 %r 就是 False
print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."
#字符串拼接
print w + e
print "加分习题"
print "第一题："
print "第二题："
binary = "binary"
do_not = "don't"
# 两次包裹
y = "Those who know %s and those who %s." % (binary, do_not)
# 两次包裹
print "I said: %r." % x
print "I also said: '%s'." % y
print "第三题：是的，看定义的变量赋值是否是字符串，格式化时候在一个字符串里面，而不是拼接"
print "w 和 e都是变量，都赋值了字符串，用+就是进行字符串拼接"
