# coding=utf-8

# 习题 15: 读取文件
# ex15.py
#把 sys 模组 import 进来
from sys import argv
# 使用 argv 来获取文件名
script, filename=argv
# 打开的文件名
txt=open(filename)
# 再次输入文件名
print "Type the filename again:"
file_again= raw_input(">>>")
# 打开后面那次输入的文件
txt_again = open(file_again)
# 读取文件内容并打印
print txt_again.read()

# 加分习题
# 8.	让你的脚本针对 txt and txt_again 变量执行一下 close() ，处理完文件后你需要将其关闭，这是很重要的一点。
txt.close()
txt_again.close()
