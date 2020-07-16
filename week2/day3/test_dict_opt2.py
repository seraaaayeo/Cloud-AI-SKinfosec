def register():
    name = str(input("이름: "))
    age = int(input("나이: "))
    major = str(input("전공: "))
    ai_dict = {"name": name, "age": age, "major": major}
    print(f"수강생 {name}의 정보가 등록되었습니다.")
    return ai_dict

def ai_list(ai_dict):
    print(ai_dict)
    return ai_dict

def ai_remove(name, ai_dict):
    for i in ai_dict:
        if(i["name"] == name):
            del ai_dict[ai_dict.index(i)]
    return print(f"수강생 {name}의 정보가 삭제되었습니다.")


def ai_update(name, ai_dict):
    for i in ai_dict:
        if(i["name"]==name):
            print("무엇을 수정하겠습니까?: 1.나이 2.전공 3.모두")
            index = int(input("번호 선택: "))
            if index == 1:
                i["age"] = int(input("나이 수정: "))
            elif index == 2:
                i["major"] = str(input("전공 수정: "))
            elif index == 3:
                i["age"] = int(input("나이 수정: "))
                i["major"] = str(input("전공 수정: "))
            else:
                print("no matching")
    return  print(f"수강생 {name}의 정보가 수정되었습니다.")

def ai_search(name, ai_dict):
    for i in ai_dict:
        if i["name"] == name:
            return i

def is_exist(name, ai_dict):
    index = 0
    for i in ai_dict:
        if i["name"] == name:
           return index
        index +=1

def main():
    i=0
    info_arr=[]
    while(1):
        print("========= AI 수강생 관리 system ========= \n1. 신규 수강생 등록\n2. 수강생 목록\n3. 수강생 삭제\n4. 수강생 정보 수정\n5. 특정 수강생 조회\n6. 수강생 등록번호 조회\n7. 종료")
        print("==========================================")
        menu = int(input("메뉴를 선택하세요: "))
        if menu == int(1):
            num = int(input("등록할 수강생 수: "))
            while i < num:
                info_arr.append(register())
                i+=1
        elif menu == int(2):
            ai_list(info_arr)
        elif menu == int(3):
            del_name = str(input("삭제할 수강생 이름: "))
            ai_remove(del_name, info_arr)
        elif menu == int(4):
            update_name = str(input("수정할 학생 이름: "))
            ai_update(update_name, info_arr)
        elif menu == int(5):
            get_name = str(input("조회할 수강생 이름: "))
            print("해당 수강생 정보: ", ai_search(get_name, info_arr))
        elif menu == int(6):
            get_name = str(input("조회할 수강생 이름: "))
            print("몇 번째로 등록한 학생인가? ", is_exist(get_name, info_arr))
        elif menu == int(7):
            print("시스템 종료")
            break
        else:
            print("no proper number: 시스템 종료")
            exit()
if __name__ == "__main__":  
    main()