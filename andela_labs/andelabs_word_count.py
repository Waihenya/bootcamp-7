def words(string):

  
    words_string = string.split()
    
    word_count = {}

    for i in words_string:
    	if i.isdigit():
    		i = int(i)
    		
    	if word_count.get(i):
            word_count[i] += 1
           
        else:
            word_count[i] = 1

    return word_count

print (words("olly 12 12 12 in come 45 free come",))