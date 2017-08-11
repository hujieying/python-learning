# _*_ coding:utf-8 _*_

from sys import argv

aaa, name= argv

print "你叫什么名字？",name
print "你的身高？："
height = raw_input()
print "你的体重？"
weight = raw_input()
print "你的年龄？"
age = raw_input()

print "个人信息：",name
print "身高：", height
print "体重：", weight
print "年龄：", age