# coding:utf-8
# 习题3：数字和数学计算
# 我现在要计算鸡群的数量 print在3.x版本里需要加上(),print(coding here)
print "I will now count my chickens:"
#母鸡 25只加上（30只除以6）等于30只，计算结果会直接输出， 字符串"Hens"需要加引号，和后面的数字类型不同所以要用,逗号分隔，但这个逗号不会被打印出来，计算顺序为先一元运算符，然后按顺序乘除余，最后加减；
print "Hens",25 + 30 / 6
#公鸡 100只减去（25乘以3除4取余）等于97只，相当于100 - ((25 * 3) % 4)
print "Roosters", 100 - 25 * 3 % 4

#现在我要计算蛋的数量
print "Now I will count the eggs:"

#3 + 2 ! - 5 + (4 % 2) - (1 /4)+ 6
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

#被双引号包裹的为字符串，会直接打印出来；
print "Is it true 3 + 2 < 5 - 7?"
#不用引号包裹，表达式会运算，做比较判断，返回布尔类型，要么为True ,要么为False; 这里的计算顺序是先计算后比较。所以就是 5 < -2进行比较，结果返回为False;
print 3 + 2 < 5 - 7

#如上所述，计算公式作为字符串被打印，后面的为表达式会将运算结果打印出来；
print "What is 3 + 2?", 3 + 2

print "What is 5 - 7?", 5 - 7


print "Oh, that's why it's False."

print "How about some more"

#这个直接返回了结果 5大于负2 ，返回True
print "Is it greater?", 5 > -2
#大于或等于 返回True
print "Is it greater or equal?", 5 >= -2
#5小于或等于-2？返回False
print "Is it less or equal?", 5 <= -2


