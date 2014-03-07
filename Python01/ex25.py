# coding=utf-8

# 习题 25: 更多更多的练习
# ex25.py

# 以空格分割字符串
def  break_words(stuff):
	"""This function will break up words for us."""	
	# 分隔符不能为空，否则会出错 ValueError: empty separator
	words = stuff.split(' ')	
	return words
# 排序
def sort_words(words):
	"""sorts the words."""
	return sorted(words)
# 打印第一个字符
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word=words.pop(0)
	print word
# 打印最后一个字符
def  print_last_word(words):
	"""Prints the last word after popping it off."""
	word=words.pop(-1)
	print word
# 对句子的单词排序
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words=break_words(sentence)
	return sort_words(words)
# 打印第一个和最后一个字符串
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words=break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words=sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

