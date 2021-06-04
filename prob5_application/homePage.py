
class Student:
  def __init__(self, name, roll,age,gender):
    self.name = name
    self.roll = roll
    self.age = age
    self.gender = gender

  def printStudent(self):
    print("Name: " + self.name +" Roll Number: " + self.roll +" Age: " + self.age +" Gender: " + self.gender )

def func_CreateData(students):
        name = raw_input('Enter Name = ')
        roll = raw_input('Enter Roll Number = ')
        age = raw_input('Enter Age = ')
        gender = raw_input('Enter Gender = ')
	
	stud = Student(name,roll,age,gender)
	students.append(stud)
        print('Data Saved Successfully')
	return students

def func_ReadData(students):

	for s in students:
  		s.printStudent()


def func_UpdateData(students):
        id = raw_input('Enter Student roll number to update = ')
	for s in students:
		if(s.roll == id):
		   print('Data Fetched for Roll number = ', id)
		   print('Roll number\t\t Name\t\t\t Age\t\t\t Gender')
		   print('-------------------------------------------')       
		   print(' {}\t\t {} \t\t\t{} \t\t\t{} '.format(s.roll, s.name, s.age, s.gender))
		   print('-------------------------------------------')
		   print('Enter New Data To Update Student Record ')

		   name = raw_input('Enter Name = ')
		   age = raw_input('Enter Age = ')
		   gender = raw_input('Enter Gender = ')
		   s.name = name
		   s.age = age
		   s.gender = gender
           	   print('Data Updated Successfully')
	
	return students



def func_DeleteData(students):
        id = raw_input('Enter Student roll number to Delete = ')
	count = 0
	for s in students:
		if(s.roll == id):
		   students.pop(count)
           	   print('Data deleted Successfully')
		count = count +1
	return students

def main():

    students = []
    while True :
	    
	    print('*****************************************************************')
	    print('Available Options: C=Create, R=Read, U=Update, D=Delete , X=Exit ')
	    choice = raw_input('Choose your option = ')

	    if choice == 'C':
		students =func_CreateData(students)
	    elif choice == 'R':
	       	func_ReadData(students)
	    elif choice == 'U':
		students =func_UpdateData(students)
	    elif choice == 'D':
		students =func_DeleteData(students)
	    elif choice == 'X':
		break
	    else:
		print('Wrong choice.')

main()
