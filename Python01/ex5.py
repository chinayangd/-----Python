# coding=utf-8

my_name= 'Zed A. Shaw'
my_age=35 #not a lie
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes= 'Blue'
my_teeth='White'
my_hair='Brown'

print "Let's talk about %s" % my_name
print "He's %d inches tall."% my_height
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee."%my_teeth

#this line is tricky, ty to get it exactly right
print "If I add %d,%d,and %d Iget %d."%(
	my_age,my_height,my_weight,my_age+my_height+my_weight)


''' 以下是加分习题 '''
''' 中文前面加u使得编码被指定为unicode，即python的内部编码以便正常显示中文'''
print "-----------------------------------------"
print u"修改所有的变量名字，把它们前面的``my_``去掉."

name= 'Zed A. Shaw'
age=35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes= 'Blue'
teeth='White'
hair='Brown'

print "Let's talk about %s" % name
print "He's %d inches tall."% height
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee."%teeth

#this line is tricky, ty to get it exactly right
print "If I add %d,%d,and %d Iget %d."%(
	age,height,weight,age+height+weight)



''' 以下是学习格式化字符串内容 '''
print "-----------------------------------------"
print u"字符串格式化"
uid = "sa"
pwd = "secret"
print "%s is not a good password for %s" % (pwd, uid)

# %d 可处理整数
userCount = 6
print "Users connected: %d" % (userCount, )

# %f 格式符选项对应一个十进制浮点数，不指定精度时打印 6 位小数
print "Today's stock price: %f" % 50.4625

# 使用包含“.2”精度修正符的 %f 格式符选项将只打印 2 位小数
print "Today's stock price: %.2f" % 50.4625
print "Change since yesterday: %+.2f" % 1.5


'''用数学计算把英寸和磅转化为厘米和千克
1英寸 = 2.54厘米，1磅 = 0.4536千克
'''
print "-----------------------------------------"
my_height_cm = my_height*2.54
my_weight_kg = my_weight*0.4536
print "His height is %s" %my_height_cm
print "His weight is %s" %my_weight_kg

'''Python 格式化字符
%d 格式化整数
%i 格式化整数
%u 格式化无符号整数（废弃，不赞成使用）
%o 格式化无符号八进制数
%X 格式化无符号十六进制数（小写字母）
%X 格式化无符号十六进制数（大写字母）
%e 用科学计数法格式化浮点数
%E 作用和%e一样
%f 格式化浮点数，可以指定小数点后的精度，默认显示6位小数，例如%.2f显示2位小数。
%F 和%f一样
%g 根据值的大小决定使用%f还是%e
%G 和%g一样
%c 格式化字符及ASCII码；
%s 格式化字符串
%r 大字符串
'''
