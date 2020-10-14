import Person import Person, Student, Staff


mike = Person("Mike", "____")
mike.Person()

mike = Student("121", 2, 30000, mike.name, mike.address)
mike.Student()

mike = Staff("111q", 89, mike.name, mike.address)
mike.Staff()
