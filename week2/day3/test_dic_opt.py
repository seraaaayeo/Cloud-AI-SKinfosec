def set_info():
    print("=====신규 정보 입력=====")
    name = str(input("이름: "))
    age = int(input("나이: "))
    major = str(input("전공: "))
    info = {"name": name, "age": age, "major": major}
    print(f"수강생 {name}의 정보가 등록되었습니다.")
    return info

def get_info(info):
    print(f"수강생:{info}")

def update_info(name, info):
    for i in info:
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

def delete_info(name, info):
    for i in info:
        if(i["name"] == name):
            del info[info.index(i)]

def main():
    i=0
    info_arr=[]
    while(1):
        print("========= AI 수강생 관리 system ========= \n1. 신규 수강생 등록\n2. 수강생 목록\n3. 수강생 삭제\n4. 수강생 정보 수정\n5. 종료")
        print("=========================================")
        menu = int(input("메뉴를 선택하세요: "))
        if menu == int(1):
            num = int(input("등록할 수강생 수: "))
            while i < num:
                info_arr.append(set_info())
                i+=1
        elif menu == int(2):
            for i in range(len(info_arr)):
                get_info(info_arr[i])
        elif menu == int(3):
            del_name = str(input("삭제할 수강생 이름: "))
            delete_info(del_name, info_arr)
            print(f"수강생 {del_name}의 정보가 삭제되었습니다.")
        elif menu == int(4):
            update_name = str(input("수정할 학생 이름: "))
            update_info(update_name, info_arr)
            print(f"수강생 {update_name}의 정보가 수정되었습니다.")

        elif menu == int(5):
            break
        
        else:
            print("no proper number")
            exit()
    
if __name__ == '__main__':
    main()
