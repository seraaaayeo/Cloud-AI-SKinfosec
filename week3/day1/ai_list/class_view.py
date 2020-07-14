def menu_display():
    print("========= AI 수강생 관리 system ========= \n1. 신규 수강생 등록\n2. 수강생 목록\n3. 수강생 삭제\n4. 수강생 정보 수정\n5. 특정 수강생 조회\n0. 종료")
    print("==========================================")

def message_display(message):
    print(message)

#ai list 출력
def ai_list_display(ai_list):
    for  val in enumerate(ai_list):
        print(f"{str(val)}")

#ai_entity 상세정보 출력
def ai_entity_display(ai_entity):
    print(f"{ai_entity.email} 상세정보: {str(ai_entity)}")

def line_display():
    print("="*30)

#ai_entity 정보입력
def input_ai_entity():
    name = input("name: ")
    age = int(input("age: "))
    major = input("major: ")
    return name, age, major

#email 정보 입력
def input_email():
    email = input("이메일을 입력하세요: ")
    return email

#menu select 정보 입력
def input_menu():
    menu = int(input("메뉴를 선택하세요: "))
    return menu