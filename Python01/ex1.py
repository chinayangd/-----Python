# coding=utf-8
#print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'

'''自己的练习：格式化输出整数'''
strHello = "The length of (%s) is %d" %('Hello World',len('Hello World'))
print strHello

'''自己的练习：格式化输出16进制整数'''
nHex = 0x20
print "nHex = %x,nDec = %d,nOct = %o" %(nHex,nHex,nHex)

for i in range(0,5):
    print i,

''' 万能的%r '''
formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
"I had this thing.",
"That you could type up right.",
 "But it didn't sing.",
 "So I said goodnight."
 )

print formatter % (
'I had this thing.',
'That you could type up right.',
 'But it didnt sing',
 'So I said goodnight'
 )