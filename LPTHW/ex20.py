# coding:utf-8
from sys import argv

script, input_file = argv

#定义print_all这个函数，变量是f，然后打印f中的内容，如果这里是文件，就打印文件内容
def print_all(f):
	print f.read()

#定义rewind这个函数，变量是f，然后对f执行seek函数
def rewind(f):
	f.seek(0)

#定义print_a_line这个函数，里面有两个变量，然后打印line_count，然后读取文件的一行
def print_a_line(line_count, f):
	print line_count, f.readline()

#打开input_file中的内容，赋给变量current_file
current_file = open(input_file)

print "First let's print the whole file:\n"

#执行函数print_all，即打印出current_file中的内容
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#执行rewind函数，
rewind(current_file)

print "Let's print three lines:"

#赋值为1
current_line = 1
#执行print_a_line这个函数
print_a_line(current_line, current_file)

#赋值为上一个current_line再加1，即应该打印为2
#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

#赋值为上一个current_line再加1，即应该打印为3
current_line = current_line + 1
print_a_line(current_line, current_file)