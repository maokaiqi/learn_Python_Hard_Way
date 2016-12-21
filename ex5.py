# -- coding:utf-8 --
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

#加分题
print "第一题;"
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # 
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name # %s是输出字符串 %d是有符号的十进制整数
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "第二题:" 
print "Let's talk about %r." % name

print "第三题："
print "%a 和 %A 是浮点数、十六进制数字和p-计数法"
print "%c 字符"
print "%d 有符号十进制整数"
print "%f 浮点数（包括float和doulbe）"
print "%e(%E) 浮点数指数输出[e-(E-)计数法]"
print "%g(%G) 浮点数不显示无意义的零‘0’"
print "%i 有符号十进制整数（与%d相同）"
print "%u 无符号十进制整数"
print "%o 八进制整数"
print "%x(%X) 十六进制整数"
print "%p 指针"
print "%s 字符串"
print "%% % 如同转义字符\\ "

print "第四题："
num = input("输入要转换的数字：")
index = input("请问你是要转换什么结果？输入数字1：英寸转换为厘米，输入数字2：磅转换为千克:")
if index == 1:
	inches_to_cm = num * 2.54
	print "您输入的 %g 英寸的转换结果为 %g 厘米。" % (num , inches_to_cm)
elif index == 2:
	lb_to_kg = num * 0.4536
	print "您输入的 %g 磅的转换结果为 %g 千克。" % (num , lb_to_kg)
else:
	print "您输入的数字有误！"



