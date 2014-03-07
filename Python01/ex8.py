# coding=utf-8

# 习题 8: 打印，打印
# ex8.py

formatter="%r %r %r %r"
print formatter %(1,2,3,4)
print formatter %("one","two","three","four")
print formatter %(True,False,False,True)
print formatter %(formatter,formatter,formatter,formatter)
print formatter %(
	"I had this thing.",
	"That you could type up riht.",
	"But it didn't sing.",
	"So I said goodnight."
	)
print formatter %('one',"two",'three','four')
# 默认使用单引号(第10行)，如果字符串中有单引号就使用双引号。如果字符串中有双引号，还是默认使用单引号。