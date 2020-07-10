'''
@function: Create
'''
def register():
    name = str(input("이름: "))
    age = int(input("나이: "))
    major = str(input("전공: "))
    ai_dict = {"name": name, "age": age, "major": major}
    print(f"수강생 {name}의 정보가 등록되었습니다.")
    return ai_dict