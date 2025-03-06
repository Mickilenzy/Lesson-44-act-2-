class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname\
        

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Ilerioluwa", "Michael", 2024)
x.printname()
print(x.graduationyear)

y = Student("Adeoye", "Daniel", 2024)
y.printname()
print(x.graduationyear)
