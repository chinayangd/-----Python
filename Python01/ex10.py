# coding=utf-8

# 10: 那是什么？(转义字符)
# ex10.py

tabby_cat ="\tI'm tabbed in."
persian_cat="I'm split\non a line."
backslash_cat="I'm \\ a \\ cat."

fat_cat="""
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip \n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


print u"--------以下为加分练习题--------"
'''上网搜索一下还有哪些可用的转义字符。
\(在行尾) 续行，表示不换行
\\ 反斜杠
\' 单引号
\" 双引号
\a 响铃
\b 退格，表示删除前面一个字符
\t 水平制表符
\v 垂直制表符，表示换行，然后从\v的地方开始输出。
\n 换行
\f 换页
'''
# ''' (三个单引号)取代三个双引号，效果同样
# 将转义序列和格式化字符串放到一起，创建一种更复杂的格式
print "backslash_cat = "+backslash_cat
backslash_cat2="I'm \\ a \\ cat \n \t* %s *." %backslash_cat
print "backslash_cat2 = "+backslash_cat2
print u"----------------"
# %r 打印出来的是你写在脚本里的内容，而 %s 打印的是你应该看到的内容
backslash_cat3="I'm \\ a \\ cat \t* %r *." %backslash_cat
print "backslash_cat3 = "+backslash_cat3
print u"----------------"
print "backslash_cat r= %r" %backslash_cat
print "backslash_cat s= %s" %backslash_cat
print u"----------------"
print "I am 6'2\" tall." # 将字符串中的双引号转义
print 'I am 6\'2" tall.' # 将字符串种的单引号转义
# 使用 %r 搭配单引号和双引号转义字符打印一些字符串出来。 
print u"----------------"
tabby_cat2 ="I'm tabbed in %r %s." %('a',"house")
print tabby_cat2
tabby_cat2 ="I'm tabbed in \"%r\" %s." %('a',"house")
print tabby_cat2
tabby_cat2 ="I'm tabbed in \"%r %s." %('a',"house")
print tabby_cat2
tabby_cat2 ="I'm tabbed in %r \'%s\'." %('a',"house")
print tabby_cat2

print r'\t\r'