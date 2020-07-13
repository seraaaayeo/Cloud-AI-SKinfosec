class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def info(self):
        print(f"아이디: {self.id}\t이름: {self.name}\n", end="")

class Student(Person):
    def __init__(self, id, name, major):
        Person.__init__(self, id, name)
        self.major = major
    def Student_info(self):
        print(f"학번: {self.id}\t이름: {self.name}\t전공: {self.major}", end="")

class Teacher(Person):
    def __init__(self, id, name, subject):
        super().__init__(id, name)
        self.subject = subject
    def Teacher_info(self):
        print(f"교번: {self.id}\t이름: {self.name}\t담당과목: {self.subject}", end="")

class Employee(Person):
    def __init__(self, id, name, department):
        super().__init__(id, name)
        self.department = department
    def Employee_info(self):
        print(f"사번: {self.id}\t이름: {self.name}\t부서: {self.department}", end="")

