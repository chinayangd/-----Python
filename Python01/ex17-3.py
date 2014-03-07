# coding=utf-8

# 习题 17: 更多文件操作
# 此程序使用追加的方式来合并两个文件内容，对原有的内容不做清除
# ex17-3.py

from sys import argv
#将文件名字符串作为参数，如果文件存在返回 True，否则将返回 False
from os.path import exists

script, from_file, to_file=argv

print "Copying from %s to %s " %(from_file, to_file)

# we could do these two on one line too, how?
input=open(from_file)
indata =input.read()

# 以读写追加模式打开：'a+'
output=open(to_file,'a+')
output.write(indata)

print "Allright, all done."
# 关闭文件，释放系统资源
output.close()
input.close()
