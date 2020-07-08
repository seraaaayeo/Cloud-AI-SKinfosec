def main():
    i=0
    arr=[]
    while(1):
        print("----메뉴를 선택하세요---- \n1. AI 수강생 등록\n2. AI 수강생 목록\n3. 수강생 삭제\n4. 수강생 정보 수정\n5. 종료")
        print("------------------------")
        menu = int(input())
        if menu == int(1):
            print("수강생 수: ")
            num = int(input())
            while i < num:
                print("정보 입력:")
                name = str(input("이름: "))
                age = int(input("나이: "))
                major = str(input("전공: "))
                info = {"name": name, "age": age, "major": major}
                arr.append(info)
                i+=1
            continue
        if menu == int(2):
            if(len(arr)==0):
                print("no student")
                break
            for i in range(len(arr)):
                print(f"수강생 {i} 정보:{arr[i]}")
                continue
        if menu == int(3):
            del_name = str(input("삭제할 수강생 이름:"))
            for i in arr:
                if(i["name"] == del_name):
                    del arr[arr.index(i)]
                else:
                    print("no matching")
        if menu == int(4):
            update_name = str(input("정보 수정할 학생 이름:"))
            for i in arr:
                if(i["name"]==update_name):
                    print("수정할 정보: 1.나이 2.전공 3.모두")
                    index = int(input())
                    if index == 1:
                        update_age = int(input("나이 수정:"))
                        i["age"] = update_age
                    elif index == 2:
                        update_name = str(input("전공 수정"))
                        i["major"] = update_name
                    elif index == 3:
                        update_age = int(input("나이 수정:"))
                        i["age"] = update_age
                        update_name = str(input("전공 수정"))
                        i["major"] = update_name
                    else:
                        print("no matching")
                        
        elif menu == int(5):
            break

if __name__ == "__main__":
    main()