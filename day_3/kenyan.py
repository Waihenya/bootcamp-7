import person

class Kenyan(person.Person):

	corrupt = False

	def probe(self, corrupt):
		self.corrupt = corrupt

	def is_corrupt(self):

		if self.corrupt:
		    return "Yes"

		return "No"
	
#to be copied in oop
