


class Hello(object):
	def __init__(self,name,age,position):
		self.name = name
		self.age = age
		self.position = position
	
	def display(self):
		return ' Name: {} \n Age: {} \n Position: {} '.format(self.name,self.age,self.position)

class Hey(Hello):
	address = ''

	def __init__(self,name,age,position,address):
		self.address = address
		super(Hey, self).__init__(name,age,position)

	def get_address(self):
		return ' Address: {}'.format(self.address)


		


x = Hey('Marion',28,'Administrator','Nairobi')
y = Hello('janni',34,'designer')

print x.display()
print x.get_address()
print y.display()







