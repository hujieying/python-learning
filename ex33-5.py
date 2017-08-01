numbers = []

# 使用range函数定义。for循环中可以使用in range(a,b,c) a->起始值，b->结束值，c->跨度（step）值
for i in range(0, 10, 2):
	print "At the top i is %d" % i
	numbers.append(i)
	
	print "Numbers now:", numbers
	print "At the bottom i is %d" % i
	
	
print "The numbers:"
	
for num in numbers:
	print num
	