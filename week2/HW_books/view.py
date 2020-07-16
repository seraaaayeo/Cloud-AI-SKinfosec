import data_io as data
import create
import read
import update
import delete

def view():
    try:
        info_arr = data.read_data("book_list.txt")
    except:
        print("No data exists")
        info_arr = []

    while(1):
        print("========= 도서 관리 system ========= \n1. 신규 도서 등록\n2. 보유 도서 조회\n3. 도서 삭제\n4. 도서 정보 수정\n5. 특정 도서 정보 조회\n6. 도서 등록번호 조회\n7. 종료")
        print("==========================================")
        menu = int(input("메뉴를 선택하세요: "))
        if menu == int(1):
            i=0
            num = int(input("등록할 도서 갯수: "))
            while i < num:
                info_arr.append(create.register())
                i+=1
        elif menu == int(2):
            read.ai_list(info_arr)
        elif menu == int(3):
            del_name = str(input("삭제할 도서 이름: "))
            delete.ai_remove(del_name, info_arr)
        elif menu == int(4):
            update_name = str(input("수정할 도서 이름: "))
            update.ai_update(update_name, info_arr)
        elif menu == int(5):
            get_name = str(input("조회할 도서 이름: "))
            print("해당 도서 정보: ", read.ai_search(get_name, info_arr))
        elif menu == int(6):
            get_name = str(input("조회할 도서 이름: "))
            print("해당 도서 등록 번호: ", read.ai_num(get_name, info_arr))
        elif menu == int(7):
            print("시스템 종료")
            data.save_list("book_list.txt", read.ai_list(info_arr))
            break
        else:
            print("no proper number: 시스템 종료")
            exit()
if __name__ == "__main__":  
    view()