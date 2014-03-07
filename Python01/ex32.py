# coding=utf-8

# 习题 32: 循环和列表
# ex32.py

# 创建列表
the_count=[1,2,3,4,5]
fruits=['apples','oranges','pears','apricots']
change=[1,'pennies',2,'dimes',3,'quarters']

# 使用for循环遍历the_count列表
# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" %number

# 使用for循环遍历fruits列表
# same as above
for fruit in fruits:
	print "A fruit of type: %s" %fruit

# 使用for循环遍历change列表
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I go %r" %i

# 创建一个空列表
# we can also build lists, first start with an empty one
elements=[]

# then use the range function to do 0 to 5 counts
#  range也是一种类型（type），它是一个数字的序列，而且是不可变的，通常用在for循环中
for i in range(0,6):
	print "Adding %d to the list." %i
	# append is a function that lists understand
	# append() 方法向列表elements的尾部添加一个新的元素
	elements.append(i)
# 以上循环可替换为：elements = range(0, 6)

# 打印列表
# now we can print them out too
for i in elements:
	print "Element was: %d" %i

print "---------------------"
for z in range(1,11,2):
    print z
else:
    print 'The for loop is over'
