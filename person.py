

class Person:
	pets = []

	def add_pet(self,pet):
		self.pets.append(pet)

jane = Person()
bob = Person()

jane.add_pet('fish')
jane.add_pet('hen')
jane.add_pet('cow')

print jane.pets
	