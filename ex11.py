# coding:utf-8
print "How old are you?",

age = raw_input()

print "How tall are you?",

height = raw_input()

print "How much do you weight?",

weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

print "加分习题"
print "1:input的特点:第一、输入字符串必须带上双引号或者单引号，否则会报错，此时输出的类型为字符串。第二、可以直接输入数字，输出的数字为整型或者浮点型。raw_input的特点：第一、输入字符串不需要带上双引号或者单引号，这样对用户更加友好，输出的类型为字符串。第二、用户如果输入数字，输出的数字会变成字符串，这样如果需要计算的话需要int()或者float()转换类型；"
num = input("输入你的名字一定要加引号：")
print type(num)

num2 = input("输入你的幸运数字：")
print type(num2)

s3 = raw_input( "输入你的名字不用加引号：")
print type(s3)

s4 = raw_input("输入你的幸运数字：")
print type(s4)
print "input要输出\' \"需要带上转义符号\\，而raw_input不需要。"


