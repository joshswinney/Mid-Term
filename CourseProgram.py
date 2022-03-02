'''
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
'''

import CourseClass as cc
import RegisterClass as rc

def main():

    name = 'MIS 4322 - Advanced Python'
    crn = '250309'
    seats = 4
    status = 'open'
    students = ['John','James','Jill','Jack','Joanne']

    course1 = cc.Course(name,crn,seats,status,students)
    

    for student in students:
       John_reg = rc.Register(name, crn, get_name)
       James_reg = rc.Register(name, crn, get_name)
       Jill_reg = rc.Register(name, crn, get_name)
       Jack_reg = rc.Register(name, crn, get_name)
       Joanne_reg = rc.Register(name, crn, get_name)

       print('Student Name: ', Register.get_name)
       print('Course Name: ', Course.getname)
       print('CRN: ', Course.get_crn)
       print('Seats left: ', Course.update_seat_count)

       if update_seat_count = 0:
          print('Sorry ', Register.get_name(), 'registration is closed for ', Course.get_name)


    
    
main()



        
    
    
