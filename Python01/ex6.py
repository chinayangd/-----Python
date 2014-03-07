# coding=utf-8

# Learn Python The Hard Way学习(6) - 字符串和文本 
# ex6.py  

# 定义一个字符串常量x，%d 表示格式化整数， %10后面的10表示要替换%d的内容
x="There are %d types of people." %10
# binary、do_not 都是字符串常量
binary="binary"
do_not="don't"
# (binary,do_not) 表示要输出包含多个格式符的话，后面的变量要用一个()包含并且用,号分隔
# %s为格式化字符串
y="Those who know %s and those who %s"%(binary,do_not)

#打印出x和y的内容
print x
print y

# 引用x和y的内容与其他字符串一起打印出来
# %r 大字符串 ，%s 格式化字符串
print "I said:%r."%x
print "I also said:'%s."%y

#定义一个布尔型常量hilarious
hilarious=False
# 定义一个字符串常量，但未定义%r的具体内容
joke_evaluation = "Isn't that joke so funny?!%r"

# 使用hilarious来替代%r
print joke_evaluation%hilarious

w="This is the left side of ..."
e="a string with a right side."
# 打印连接字符串
print w+e



''' ”字符串包含字符串”的位置
    y="Those who know %s and those who %s"%(binary,do_not)
    print "I said:%r."%x
	print "I also said:'%s."%y
'''

# 字符串是用单引号或者双引号包括起来的