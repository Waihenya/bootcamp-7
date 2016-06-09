class Student(object):
    '''Creates student instances '''
     units = {
        'CS001': {'unit_name': 'Computer Literacy', 'core': True},
        'CS002': {'unit_name': 'Communication Skills', 'core': False},
        'CS003': {'unit_name': 'Introduction to Programming', 'core': False},
        'CS004': {'unit_name': 'Introduction to Computers', 'core': True},
        'CS005': {'unit_name': 'Discrete Mathematics', 'core': True} 
            }
   

    def __init__(self, fname, lname, student_id):
        # initialize every student instance created for class Student
      
        
         self.fname = fname
         self.lname = lname
         self.student_id = student_id
         self.units = []
       
    
    def get_student_details(self):
        # display student details including name, ID No and units enrolled for
        return ' Student Name: {} {} \n Reg No: {} \n Units Enrolled: {}'.format(self.fname,self.lname,self.student_id,self.units)
    
    def enroll_unit(self,unit_code):
        # enrol a particular student for a given unit

        if units[unit_code]["core"]==True:
            self.units.append(unit_code)
             
        else:
          return 'Not a core unit'
           
        

    def get_enrolled_units(self):
        # display all the units a student has enrolled for
         for u in self.units:
            for key , value in self.units.items():
                if u in key:
                    print u + ' : ' + value['unit_name']
      
    
#testing 

new_student = Student('Joe','N','ST101-2016')


print new_student.get_student_details()
print new_student.enroll_unit('CS005')
print new_student001.get_enrolled_units()

