import class_controller
from class_domain import AIEntity
import class_view as view
controller = class_controller.AIController() #인스턴스로 참조

controller.file_read()

while True:
    view.menu_display()

    menu = view.input_menu()

    if menu == int(1):
        email = view.input_email()
        name, age, major = view.input_ai_entity()
        controller.register_controller(AIEntity(name, age, email, major))
    
    elif menu == int(2):
        controller.get_all_entity()

    elif menu == int(3):
        email = view.input_email()
        controller.delete_controller(email)

    elif menu == int(4):
        emil = view.input_email()
        name, age, major = view.input_ai_entity()
        controller.update_controller(AIEntity(name, age, email, major))
    
    elif menu == int(5):
        email = view.input_email
        controller.get_entity_controller(email)

    elif menu == int(0):
        view.message_display("시스템 종료")
        controller.file_write()
        break
    
    else:
        view.message_display("no proper number: 메뉴는 1,2,3,4,5중 하나를 선택하고 종료는 0을 선택")
        continue