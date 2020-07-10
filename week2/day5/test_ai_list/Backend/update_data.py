'''
@function: Update data
'''
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
    