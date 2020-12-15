import Person import Person, Student, Staff


tom = Person("Tom", "____")
tom.Person()

tom = Student("121", 2, 30000, tom.name, tom.address)
tom.Student()

tom = Staff("111q", 89, tom.name, tom.address)
tom.Staff()
