# coding=utf-8

# 习题 16: 读写文件
# ex16.py

from sys import argv

script, filename=argv

print "We're going to erase %r" %filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target=open(filename,'w')

print "Truncating the fine. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1=raw_input("line1:")
line2=raw_input("line2:")
line3=raw_input("line3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
# 加分练习题
# 使用 read 和 argv 读取你刚才新建的文件
print "-------------------------"
target=open(filename,'a')
# 想办法只使用一个target.write()代替上面的6行
line1=raw_input("line1:")
line2=raw_input("line2:")
line3=raw_input("line3:")
line = "%s\n%s\n%s\n" % (line1, line2, line3)
target.write(line)
target.close()
print "-------------------------"
target=open(filename,'r')
print target.read()
target.close()

