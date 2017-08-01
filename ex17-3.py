# coding:utf-8
from sys import argv

script, from_file, to_file = argv

#倒着看这行代码，原理是先open打开被复制的文件，然后read读取其中的内容；
#然后写入到复制后的文件中，复制后的文件也要以可写的状态打开。
open(to_file,'w').write(open(from_file).read())

#最后应该有一个close关闭文件比较好