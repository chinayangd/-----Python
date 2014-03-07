# coding=utf-8

# 习题 42: 物以类聚
# 内容是类和对象
# ex42.py

class TheTing(object):
	"""docstring for TheTing"""
	def __init__(self):
		#super(TheTing, self).__init__()
		self.number = 0

	def some_function(self):
		print "I got called."
		
	def add_me_up(self,more):
		self.number+=more
		return self.number
	
# two different things
a=TheTing()
b=TheTing()

a.some_function()
b.some_function()

print a.add_me_up(20)
print b.add_me_up(30)

print a.number
print b.number

# Study this. This is how you pass a variable from one class to another. You will need this.
class TheMutiplier(object):
	"""docstring for TheMutiplier"""
	def __init__(self, base):
	# 	super(TheMutiplier, self).__init__()
		self.base = base

	def do_it(self, m):
		return m*self.base

x= TheMutiplier(a.number)
print x.do_it(b.number)

# 以下是重写练习41的内容，使用类

## Animal is-a object(yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

# 继承Animal类
class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self, name):
		#super(Dog, self).__init__()
		self.name = name
		
class Cat(Animal):
		"""docstring for Cat"""
		def __init__(self, name):
		#	super(Cat, self).__init__()
			self.name = name
			self.pet=name

class Person(object):
	"""docstring for Person"""
	def __init__(self, name):
		#super(Person, self).__init__()
		self.name = name
		

class Employee(Person):
	"""docstring for Employee"""
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary
		

#子类继承父类
class Fish(object):
	pass

class Salmon(Fish):
	pass	

class Halibut(Fish):
	pass	

# 类的实例化
## rover is-a Dog
rover=Dog("Rover")

satan=Cat("Satan")

mary=Person("Mary")

mary.pet=satan

frank=Employee("Frank",120000)

frank.pet=rover

flipper=Fish()

crouse=Salmon()

harry=Halibut()

