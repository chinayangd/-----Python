# coding=utf-8

# 习题 17: 更多文件操作

# 加分练习题
# 3. 看看你能把这个脚本改多短，我可以把它写成一行。
from sys import argv;open(argv[2],'w').write(open(argv[1]).read())