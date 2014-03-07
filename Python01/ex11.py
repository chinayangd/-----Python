# coding=utf-8

# 习题 11: 提问
#  ex10.py

print "How old are you?",
# 读取输入的字符串
age=raw_input()
print "How tall are you?",
height=raw_input()
print "How much do you weiht?",
weiht=raw_input()

print "So, you're %r old,%r tall and %r heavy."%(age,height,weiht)


print "How old are you?",
# 读取输入的字符,如果输入的是 28+1 ，则输出 29
age2=input()
print "you're %r old"%age2

# 加分习题
# 你能找到它的别的用法吗？测试一下你上网搜索到的例子
age3=raw_input(">>>How old are you?")
print "You are %r old."%age3

doing=raw_input("what are you doing?")
print "what are you doing?\n%r"%doing
today=raw_input("What Date is today?")
print "What Date is today? \n%r"%today