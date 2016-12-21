#coding:utf-8
#定义变量：将等号（赋值）右边的值赋给左边的变量名称。
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
#右边可以为表达式；
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#变量和字符串需要用逗号分开
print "There are", cars + 4 , "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
#加分题
#之所以出现加分习题中的错误，是因为NameError变量名错误所致，car_pool_capacity这个变量名并没有定义，定义了的是carpool_capacity。
#1：没有必要，因为人的最小计数就是个位；
#2：浮点数4.0 整数4
#3：
#4： x = 4 给变量名赋值为4
#5： Learn_Python_the_Hard_Way
#6:  y = 5 , x + y
x = 4
y = 6
i = 9
print "x*y%i的结果是：",x * y % i

