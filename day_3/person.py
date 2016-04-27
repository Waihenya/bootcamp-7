class Person(object):
	"""docstring for Person"""
	counter = 0 #|class variable
	def __init__(self, fname,age):
		#instance variable
		self.fname=fname
		#if age!=0 then...
		self.age=age
		Person.counter+=1
	def __repr__(self):
		return "< Object:{} and {} >".format(self.fname,self.age)

	def say_hello(self):
		return "Hello, I'm {} and {} years old".format(self.fname,self.age)