

def ai_update(name, ai_dict):
    for i in ai_dict:
        if(i["Product name"]==name):
            print("무엇을 수정하겠습니까?: 1.상품명 2.가격 3.상세정보 4.모두")
            index = int(input("수정할 번호 선택: "))
            if index == 1:
                i["Product name"] = str(input("상품 이름 수정: "))
            elif index == 2:
                i["Price"] = int(input("가격 수정: "))
            elif index == 3:
                i["Description"] = str(input("상세정보 수정: "))
            elif index == 4:
                i["Product name"] = str(input("상품 이름 수정: "))
                i["Price"] = int(input("가격 수정: "))
                i["Description"] = str(input("상세정보 수정: "))
            else:
                print("no matching")
    return  print(f"도서 {name}의 정보가 수정되었습니다.")
