def funky(x,y):
	if type(x) == int and type(y)== int:
		print x+y
	elif type(x) == float and type(y)== float:
		print x+y
	elif type(x) == str and type(y) == str:
		print x+y
	elif type(x)== list and type(y) == list:
		print x+y
	elif type(x) == dict and type(y) == dict:
		a_dict=dict(x.items() + y.items())
		print a_dict
	        print "Your arguments are a dictionary, ask me how I know that"
	else:
	    print "invalid input"
	    
funky(78,0)
funky(30.2,23.2)
funky("Andela ","Bootcamp")
funky([2,5,6],[34,78,90])
funky({'1':'Beatrice'},{'2': 'Waihenya'})