# _*_ coding:utf-8 _*_
from sys import argv

script, filename = argv 
    
txt = open(filename) 
print txt.read()