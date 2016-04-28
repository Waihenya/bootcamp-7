def data_type(number):
  
  if number == str:
    
    return number(len)
    
  elif number is  None:
    
    return "No value"
    
  elif number == bool:
    
     return number
     
  elif number == int:
    
    if number == 100:
      return "Equal to 100"
    
    elif number < 100:
      
      return "less than 100"
      
    else: 
      
      return "more than 100"
    
      
    return number
    
  elif number == list:
    
    if number is None:
      
      return "list empty"
      
    else:
      return number[2]

data_type(30)
