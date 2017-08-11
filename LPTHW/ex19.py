# coding:utf-8
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

#可以直接给函数传递数字
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#可以直接将值赋给函数的参数
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#全局变量？
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#函数的参数可以是数学运算
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#变量和数学结合运算作为函数的参数
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)