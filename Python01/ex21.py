# coding=utf-8

# 习题 21: 函数可以返回东西
# ex21.py

def add(a,b):
	print "ADDING %d + %d" %(a,b)
	return a+b

def subtract(a,b):
	print "SUBTRACTING %d -%d" %(a,b)
	return a-b

def multiply(a,b):
	print "MULTIPLYING %d * %d" %(a,b)
	return a*b

def divide(a,b):
	print "DIVIDING %d / %d" %(a,b)
	return a/b
print "Let's do some math with just functions!"

age= add(30,5) 		# age=35
height=subtract(78,4)	# height=74
weight= multiply(90,2)	# weight=180
iq=divide(100,2)		# iq=50

print "Age: %d, Height: %d, Weight:%d, IQ: %d" %(age,height,weight,iq)

print "------------------------------"
# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."
# divide(iq,2)=divide(50,2)=25
# multiply(weight,divide(iq,2))=multiply(180,25)=4500
# subtract(height,multiply(weight,divide(iq,2)))=subtract(74,4500)=-4426
# add ()=35+(-4426)=-4391
what= add(age,subtract(height,multiply(weight,divide(iq,2))))

print "That becomes:", what, "Can you do it by hand?"
