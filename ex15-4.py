# _*_ coding:utf-8 _*_
#前两行使用argv获取文件名
from sys import argv

script, filename = argv

#open命令，它会接收一参数，并且返回一个值，你可以将这个值赋给一个变量。这就是打开文件的过程。
txt = open(filename)

#打印一行内容
print "Here's your file %r:" % filename
#.read表示执行read命令，无需任何参数，这里就是读出txt中的内容
print txt.read()