# coding=utf-8

#习题 20: 函数和文件
# ex20.py

from sys import argv

script, input_file=argv

def print_all(f):
	print f.read()	#读取文件

def rewind(f):
	f.seek(0)	#设置文件的当前位置偏移量为0

# 读取文件的行数
def print_a_line(line_count,f):
	print line_count,f.readline()

# 打开文件，作为当前文件
current_file=open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)		# 打印当前文件

print  "Now let's rewind, kind of like a tape."
rewind(current_file) #设置当前文件的当前位置偏移，偏移量为0

print "Let's print three lines:"
current_line=1
# 打印当前文件的第一行
print_a_line(current_line,current_file)
# 打印下一行
current_line=current_line+1
print_a_line(current_line,current_file)
# 打印再下一行
current_line=current_line+1
print_a_line(current_line,current_file)
