from lan22 import Person, Student, Staff 

student = Person("oleg","nova")
student1 = Student('ol','def',"program",1,1.2)
student = Staff (student.name,student.address,'tsvitkiska',10.5)
student1.string()
student.string()