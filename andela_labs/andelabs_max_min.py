
def find_max_min(a):
  min_value = min(*a)
  max_value = max(*a)
    
  x = len(a)
  b =[]
  c =[]
    

   
  if min_value == max_value:
      
    c.append(x)
      
    return c
        
  else:
    b.append(min_value)
      
    b.append(max_value)
    
    return b
   