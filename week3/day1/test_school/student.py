
class Student:
    def __init__(self, id, name, major):
        self.id = id
        self.name = name
        self.major = major
    def Student_info(self):
        print(f"학번: {self.id}\t이름: {self.name}\t전공: {self.major}")

class Teacher:
    def __init__(self, id, name, subject):
        self.id = id
        self.name = name
        self.subject = subject
    def Teacher_info(self):
        print(f"교번: {self.id}\t이름: {self.name}\t담당과목: {self.subject}")

class Employee:
    def __init__(self, id, name, department):
        self.id = id
        self.name = name
        self.department = department
    def Employee_info(self):
        print(f"사번: {self.id}\t이름: {self.name}\t부서: {self.department}")


# ai01 = Student("ai01", "여다솔", "정보통신공학")
# ai01.Student_info()

# t001 = Teacher("T001", "최재호", "파이썬")
# t001.Teacher_info()

# e001 = Employee("E001", "여다솔", "AI개발")
# e001.Employee_info()