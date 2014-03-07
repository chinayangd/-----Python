# coding=utf-8

#打印字符串
print "I will now count my chickens:"
#打印字符串，和运算结果，/为除法，%为取余
print "Hens", 25+30/6
print "Roosters", 100-25*3%4

#打印字符串
print "Now I will count the eggs:"

#运算结果
print 3+2+1-5+4

print "Is it true that 3+2<5-7?"

#做布尔比较运算
print 3+2<5-7

#分别计算左边和右边的结果
print "What is 3+2?",3+2
print "What is 5-7?",5-7

print "Oh, that's why it's False."

print "How about some more."

#打印出运算结果为True or False
print "Is it greater?",5>-2
print "Is it greater or equal?",5>=-2
print "Is it less or equal?",5<=-2

''' 以下是自己写的运算练习 '''
''' 中文前面加u使得编码被指定为unicode，即python的内部编码以便正常显示中文'''
print "-----------------------------------------"
print u"自编的运算练习"

import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')   #修改默认编码方式，默认为ascci 
print sys.getdefaultencoding()  #打印出当前的编码方式


Total=18.98+35+22+28+(7.2*3-10)*5
print u"沃尔玛购物：Total=",Total
print "18.98+35+22+28+(7.2*3-10)*5>=100?",18.98+35+22+28+(7.2*3-10)*5>=100

#取整运算
minus=Total//100
print u"信用卡付款，满100减10,minus=", minus

Pay=Total-minus*10
print u"实际扣款,Pay=", Pay



''' 使用浮点数重写一次习题'''
print "-----------------------------------------"
print u"使用浮点数重写一次习题ex3.py."
print "I will now count my chickens:"
print "Hens", 25.0+30.0/6
print "Roosters", 100.0-25.0*3%4

print "Now I will count the eggs:"
print 3.0+2.0+1-5+4

print "Is it true that 3+2<5-7?"
print 3.0+2.0<5.0-7.0

print "What is 3+2?",3.0+2.0
print "What is 5-7?",5.0-7.0

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?",5.0>-2.0
print "Is it greater or equal?",5.0>=-2.0
print "Is it less or equal?",5.0<=-2.0
