# coding=utf-8

# 习题 17: 更多文件操作
# ex17.py

from sys import argv
#将文件名字符串作为参数，如果文件存在返回 True，否则将返回 False
from os.path import exists

script, from_file, to_file=argv

print "Copying from %s to %s " %(from_file, to_file)

# we could do these two on one line too, how?
input=open(from_file)
indata =input.read()

print "The input file is %d bytes long" %len(indata)

print "Does the output file exist?%r" %exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

output=open(to_file,'w')
output.write(indata)

print "Allright, all done."
# 关闭文件，释放系统资源
output.close()
input.close()

# 加分练习题
# 3. 看看你能把这个脚本改多短，我可以把它写成一行。
# from sys import argv;open(argv[2],'w').write(open(argv[1]).read())
