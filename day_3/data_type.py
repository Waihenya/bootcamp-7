def data_type(x):
	'''
	Takes in a n argument , x:
	    -For a integer, return x ** 2
	    -For a float, return x / 2
	    -For a string, return "hello" + x
	    -For a boolean, return "boolean"
	    -For a long, return squareroot(x)

	'''
	if type(x) == int:
		return x ** 2
	elif type(x) == float:
		return x / 2
	elif type(x) == str:
		return "Hello" + x
	elif type(x) == bool:
		return "Boolean"
	elif type(x) == long:
		return "Long"
	else:
		return "Error"

print data_type(4)
print data_type(54.2)
print data_type("Andela")
print data_type(True)
print data_type(4530987773333)

