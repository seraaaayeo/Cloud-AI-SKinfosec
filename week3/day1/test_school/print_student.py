import student
import inheritance

# 그냥 클래스 출력
ai_list1 = [student.Student("ai01", "여다솔", "정보통신공학"), student.Teacher("T001", "여다","파이썬"), student.Employee("E001", "다봄", "AI개발")]

for i in ai_list1:
    if(isinstance(i, student.Student)):
        i.Student_info()
    elif(isinstance(i, student.Teacher)):
        i.Teacher_info()
    elif(isinstance(i, student.Employee)):
        i.Employee_info()
    else:
        print("Input Error")


# 상속 클래스
ai_list2 = [inheritance.Student("ai01", "여다솔", "정보통신공학"), inheritance.Teacher("T001", "여다","파이썬"), inheritance.Employee("E001", "다봄", "AI개발")]

for i in ai_list2:
    i.info()

