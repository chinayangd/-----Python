# coding=utf-8

# 习题 33: While 循环
# ex33.py

i=0
numbers =[]

while i<6:
	print "At the top i is %d" %i
	# append 向列表的尾部添加一个新的元素
	numbers.append(i)

	i=i+1
	print 'Numbers now:', numbers
	print "At the bottom i is %d" %i

print "The numbers:"

for num in numbers:
	print num

# 加分练习题
# 1. 将这个 while 循环改成一个函数，将测试条件(i < 6)中的 6 换成一个变量。
print "--------------------------------------"
def while_function(x):
	y=0
	numbers =[]

	while y<x:
		numbers.append(y)
		y=y+1

	return numbers	
numbers=while_function(6)
print numbers

# 3. 为函数添加另外一个参数，这个参数用来定义第 8 行的加值 + 1 ，这样你就可以让它任意加值了。

print "--------------------------------------"
def while_function(x,increment):
	y=0
	numbers =[]

	while y<x:
		numbers.append(y)
		y=y+increment

	return numbers	
numbers=while_function(10,2)
print numbers

# 5. 接下来使用 for-loop 和 range 把这个脚本再写一遍。
print "--------------------------------------"
def  for_function(x,increment):
	numbers =[]
	pass

	for y in range (0,x,increment):
		numbers.append(y)

	return numbers

numbers=for_function(10,2)
print numbers

