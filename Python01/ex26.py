# coding=utf-8

# 习题 26: 恭喜你，现在可以考试了！
# 这个练习的目的是修正现有的程序
# ex26.py

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""  
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last_words(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5   # five=6
print "This should be five: %d" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" %start_point
print "We'd have %d jeans, %d jars, and %d crates." %(beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." %secret_formula(start_point)

print "--------------"
sentence = "All good\tthings come to those who weight."
print "The sentence is :%r" %sentence

# 直接使用上面定义的函数，不需要引用其他文件定义的函数
# import ex25
# words = ex25.break_words(sentence)
# sorted_words = ex25.sort_words(words)

# 拆分句子，返回单词
words = break_words(sentence)
# 把拆分句子后的单词排序
sorted_words = sort_words(words)

print u"拆分句子后的第一个单词是：",
# 打印拆分后的第一个单词
print_first_word(words)
print u"拆分句子后的最后一个单词是：",
# 打印拆分后的最后一个单词
print_last_word(words)

# 打印出句子单词排序的结果
print u"句子排序的结果是："
# 把句子的单词排序（先拆分后排序），并打印出来
sorted_words = sort_sentence(sentence)
print sorted_words

print u"句子单词排序后的第一个单词是：",
# 打印排序后的第一个单词
print_first_word(sorted_words)
print u"句子单词排序后的最后一个单词是：",
# 打印排序后的最后一个单词
print_last_word(sorted_words)

print u"打印句子的第一个和最后一个单词："
# 打印句子的第一个和最后一个单词
print_first_and_last_words(sentence)
print u"打印句子单词排序后的第一个和最后一个单词："
# 打印排序后的第一个和最后一个单词
print_first_and_last_sorted(sentence)





