# coding=utf-8

# 习题 41: 来自 Percal 25 号行星的哥顿人(Gothons)
#  这里的内容应该是面向对象
# ex41.py
# 不知道哪里错了，运行不了
'''
Traceback (most recent call last):
  File "ex41.py", line 80, in <module>
    question, answer= convert(snippet,phrase)
ValueError: need more than 0 values to unpack
'''

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS=[]

# 创建一个字典
PHRASES={
	"class ###(###):": "Make a class named ### that is-a ###",
	"class ###(object):\n\tdef__init__(self,***)": "class ### has-a __init__ that takes self and *** parameters.",
	"class ###(object):\n\tdef ***(self,@@@)": "class ### has-a function named *** that takes self and @@@ parameters.",
	"***= ###()": "Set *** to an instance of class ###.",
	"***.***(@@@)": "From *** get the *** function, and call it with parameters self, @@@.",
	"***.***='***'": "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST=False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASES_FIRST=True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())

def convert(snippet,phrase):
	# class_names =  [w.capitalze() for w in random.sample(WORDS,snippet.count("###"))]
	# other_names = random.sample(WORDS,snippet.count("***"))
	# results =[]
	# param_names=[]
	class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("###"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		param_count= random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS,param_count)))

		for sentence in snippet, phrase:
			result = sentence[:]		

		# fake class names
		for word in class_names:
			result= result.replace("###", word, 1)

		# fake other names
		for word in other_names:
			result=result.replace("***",word,1)

		# fake parameter lists
		for word in param_names:
			result= result.replace("@@@",word, 1)

		results.append(result)

	return results

# keep going until they hit CTRL-D
try:
	while  True:
		snippets=PHRASES.keys()		# 获取PHRASES字典列表	
		random.shuffle(snippets)    # 将列表中的元素打乱
		# print snippets  # 这里还能打印出列表的内容，后面是为什么呢？
		for snippet in snippets:
			phrase=PHRASES[snippet]
			question, answer= convert(snippet,phrase)
			if PHRASE_FIRST:
				question,answer = answer, question

			print question

			raw_input(">>>")
			print "ANSWER: %s\n\n" %answer
except EOFError, e:
	print "\nBye"

