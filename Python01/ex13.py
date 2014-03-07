# coding=utf-8

# 习题 13: 参数、解包、变量
# ex13.py

#把 sys 模组 import 进来
from sys import argv
#把 argv 中的东西解包，将所有的参数依次赋予左边的变量名
script, first, second, third = argv

print "The script is called:",script
print "Your first variable is:",first
print "Your second variable is:",second
print "Your third variable is:",third

#加分练习题
# 3.将 raw_input 和 argv 一起使用，让你的脚本从用户手上得到更多的输入
from sys import argv
script, a1st =argv
# 这里取来显示的是第二个参数
print "The first one is: %s" %a1st
b2nd=raw_input("And the second one is:")
print "The first one is: %s, and the second one is %s"%(a1st,b2nd)
