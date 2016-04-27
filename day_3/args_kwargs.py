#unpacking
def hello(name,age,position):
	'''
	 Explains ...

	'''
	return "I am {}, {} years old and I am a {}".format(name,age,position)

people = [("James",30,"Banker"),("Hann",90,"Farmer"),("Joan",23,"Programmer")]
 
for i in people:
	print hello(*i)

'''
    for  name,age in people:
    	print hello(name,age) 
'''
