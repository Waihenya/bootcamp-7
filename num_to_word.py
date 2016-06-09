
def num_word(A):
	'''
	 outputs the digits of the number passed in words.
	 e.g num_to_word(438483478) should output four three eight four eight three four seven eight

	'''
	A = str(A)

	words = []
	units = { '0': 'zero','1':'one', '2':'two','3':'three','4':'four','5':'five','6':'six',

                '7':'seven', '8':'eight','9':'nine'

	}
	for x in A:
		if x in units:
			words.append(units[x])
		else:
			words.append(x)

	print " ".join(words)

print num_word(3456)


'''
def num_to_words(n):
	ls = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
	for x in str(n):
		print ls[int(x)],

print num_to_words(44377777888)

'''