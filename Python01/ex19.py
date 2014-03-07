# coding=utf-8

# 习题 19: 函数和变量
# ex19.py

# 定义一个函数，包含2个参数
def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print "You have %d cheese!" %cheese_count
	print "You have %d  boxes of crackers!" %boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
# 函数参数可使用常量
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese=10
amount_of_crackers=50
# 前面定义的参数值传入函数中
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do math inside too:"
# 参数中的常量也可以做运算
cheese_and_crackers(10+20,5+6)

print "And we can combine the two, variables and math:"
# 参数可以把变量和运算结合起来
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)


# 加分习题
# 3. 自己编至少一个函数出来，然后用10种方法运行这个函数

def money(currency,amount):
	print "I have %d %s money.\n"%(amount,currency)

money("RMB",10000)

currency="CAD"
amount=20000
money(currency,amount)

money("EUR", 30000)

money("GBP", 30000+10000)

money(currency="INR",amount=50000)

currency2=money(currency="INR",amount=50000)
money(currency2, 60000)

print "money~ money~ ", money

money(money, 70000)

money(str(currency2), 80000)

print money("EUR", 90000)
