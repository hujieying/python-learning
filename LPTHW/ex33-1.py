# coding:utf-8
# 将这个while循环写成一个函数，将测试条件（i < 6）中的6换成一个变量。
# 使用这个函数重写脚本，并用不同的数进行测试。
# 添加另一个参数，定义第八行的+1，这样可以让它任意递增。


i = 0
numbers = []
maxium = int(raw_input("please input a number!\n"))
step = int(raw_input("please input a step!\n"))

while i < maxium:
    print ("At the top i is %d" % i)
    numbers.append(i)

    i += step
    print ("Numbers now:", numbers)
    print ("At the bottom i is %d" % i)

print ("The numbers:")

for num in numbers:
    print (num)