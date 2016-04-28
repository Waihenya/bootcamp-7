def data_type(a):
  
    if a is  None:
      return "no value"
      
    elif type(a) == str:
      return len(a)
      
    elif type(a) == bool:
      return a
      
    elif type(a) == int:
    
        if a >= 100:
            return "more than 100"
        else: 
            return "less than 100"
            
    elif type(a) == list:
        if len(a) < 3:
            return None
        else:
            return a[2]
    
    
print data_type(3)
print data_type(200)
print data_type('andela')
print data_type([1,2,3])
print data_type([1,2])
print data_type(True) 