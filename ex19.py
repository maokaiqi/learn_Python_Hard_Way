#coding:utf-8
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheese!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
#我们可以直接把数字作为参数
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# 参数可以是变量
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 参数可以是数学运算
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# 运行这个函数 ，参数可以使是变量和数字做数学运算
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)
