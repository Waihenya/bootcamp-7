def string_length(a):

	if type(a) == str:
	  
		return [len(a)]

	elif type(a) == list:
	  
		m = []
		for i in a:
		  
			if type(i) == str:
			  
				m.append(len(i))
				
			else:
			  
				return "Please enter a valid list of strings"
				
		return m
		
	else:
	  
		return "Please add a string or a list of strings"


print string_length('Godson')
print string_length('Mia')
print string_length(['Adam', 'Frankel'])
print string_length(['Michael', 'William', 'Smith'])
print string_length([3, 4])