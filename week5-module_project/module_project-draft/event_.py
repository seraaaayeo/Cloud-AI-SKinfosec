# GUI의 버튼 클릭으로 발생하는 여러 이벤트를 처리하는 함수 모듈입니다.

import controller_
import time
import service
import GUI_windows
from domain import ClubEntity, ClubMembershipEntity, MemberEntity
controller = controller_.VaildDataCheck()


# 레코드의 list들을 받아 하나의 스트링으로 만든다.
def text_list_out(list_, height_start):
    height_ = height_start

    text_ = ""
    for value in list_:
        text_ += ("{0}\n".format(str(value)) )
        height_ += 20

    return text_, height_


# 등록 여부를 확인하기 위해 ID를 받는다.
def window_input(key_name):
    win = GUI_windows.SubWindow_1()
    win.text_ID = key_name
    win.initUI()
    r = win.showModal()
    key = win.line_1.text()

    return r, key

# ID값을 받아서 확인된 entity 값을 return 해준다.
def register_check(key, table_name):

    bm = service.ClubService()
    result_entity = bm.is_exist(key, table_name)

    return result_entity


# entity 값을 입력받아 테이블에 추가한다.
def register_entity(key, table_name):
    register_win = GUI_windows.RegisterCommunityMember()
    message_ = "취소 하셨습니다."
    r = register_win.showModal()
    if(r and table_name == "member_"):
        email = key
        name = register_win.line_1.text()
        phone_number = register_win.line_2.text()
        birthday = register_win.line_3.text()

        message_ = controller.register_controller(email, MemberEntity(email, nickName, phoneNumber, birthday), "member_")
    elif(r and table_name == "club_"):
        clubID = key
        name = register_win.line_1.text()
        phone_number = register_win.line_2.text()
        foundation_date = register_win.line_3.text()
        address = register_win.line_4.text()

        message_ = controller.register_controller(clubID, ClubEntity(clubID, clubName, foundation_date), "club_")

    return message_


# 해당 메뉴(멤버/클럽)에서 멤버쉽 등록.
def register_membership(register_type, my_key):

    message_ = "취소 하셨습니다." 
    if(register_type == "member"):
        search_table = "club_"
    elif(register_type == "club"):
        search_table = "member_"

    win_ = GUI_windows.RegistMembership()
    win_.initUI(search_table, '0', 0)
    r = win_.showModal()

    lists_ = controller.get_all_entity_controller("membership_", "0", 0)
    key_val = len(lists_) + 100
    time_now_ = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    if(r and register_type == "member"):
        clubID = win_.line_1.text()
        message_ = controller.register_controller(key_val, ClubMembershipEntity(key_val, clubID, my_key, "member", time_now_), "membership_")

    elif(r and register_type == "club"):
        member_email = win_.line_1.text()
        message_ = controller.register_controller(key_val, ClubMembershipEntity(key_val, my_key, member_email, "member", time_now_), "membership_")

    return message_


# 해당 메뉴(멤버/클럽)에서 entity값 수정.
def modify_entity(modify_type, entity):
    message_ = "취소 하셨습니다." 

    if(modify_type == "member"):
        win_ = GUI_windows.ModifyMember()
    elif(modify_type == "club"):
        win_ = GUI_windows.ModifyClub()

    win_.initUI(entity)
    r = win_.showModal()
    if(r and modify_type == "member"):
        email_ = entity["email"]
        name = win_.line_1.text()
        phone_number = win_.line_2.text()
        birthday = win_.line_3.text()

        message_ = controller.update_controller(email_, MemberEntity(email_, name, phone_number, birthday), "member_")

    elif(r and modify_type == "club"):
        clubID_ = entity["clubID"]
        name = win_.line_1.text()
        phone_number = win_.line_2.text()
        foundation_date = win_.line_3.text()
        address = win_.line_4.text()

        message_ = controller.update_controller(clubID_, ClubEntity(clubID_, clubName, foundationDate), "club_")

    return message_



# 해당 메뉴(멤버/클럽)에서 멤버쉽 탈퇴.
def remove_membership(key, key_name):
    message_ = "취소 하셨습니다."

    win_ = GUI_windows.DeleteMembership()
    win_.initUI("membership_", str(key), key_name)
    if(win_.showModal()):
        membershipID = win_.line_1.text()
        message_ = controller.delete_controller(membershipID, "membership_")

    return message_



