# coding:utf-8
people = 30
cars = 40
buses = 15

#如果满足条件车大于人，则输出
if cars > people:
	print "We should take the cars."
#或者如果车小于人，则输出
elif cars < people:
	print "We shoud not take the cars."
#或者前面两者都不满足，则输出
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."
	
if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."
	
if cars > people and buses > cars:
	print "这是第一条"
else:
	print "这是第二条"