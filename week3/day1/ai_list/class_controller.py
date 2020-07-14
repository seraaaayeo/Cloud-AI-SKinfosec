#View에서 입력된 데이터 체크, service의 buisness method 호출, 호출된 결과값 저장, view select
from class_view import message_display, ai_list_display, ai_entity_display
import class_service as service

class AIController:
    def register_controller(self, ai_entity):
        #email valid check - regular express사용 email 형식 체크
        if ai_entity.email == "" or len(ai_entity.email)==0:
            message_display("잘못된 이메일 형식")
        else:
            #buisness method delegation
            bm = service.AIService()
            message = bm.register(ai_entity)

            #view select
            message_display(message)
    
    def get_all_entity(self):
        bm = service.AIService()
        ai_list = bm.get_all_entity()
        #view select
        ai_list_display(ai_list)

    def update_controller(self, ai_entity):
        #email valid check - regular express사용 email 형식 체크
        if ai_entity.email == "" or len(ai_entity.email)==0:
            message_display("잘못된 이메일 형식")
        else:
            #buisness method delegation
            bm = service.AIService()
            message = bm.entity_update(ai_entity)
            #view select
            message_display(message)

    def delete_controller(self, email):
        #email valid check - regular express사용 email 형식 체크
        if email == "" or len(email)==0:
            message_display("잘못된 이메일 형식")
        else:
            #buisness method delegation
            bm = service.AIService()
            message = bm.entity_remove(email)
            #view select
            message_display(message)

    def get_entity_controller(self, email):
        #email valid check - regular express사용 email 형식 체크
        if email != None:
            message_display("잘못된 이메일 형식")
        else:
            #buisness method delegation
            bm = service.AIService()
            ai_entity = bm.get_ai_entity(email)
            if ai_entity.email != None:
                ai_entity_display(ai_entity)
            else:
                message_display("존재하지 않습니다.")
    
    def file_read(self):
        bm = service.AIService()
        bm.read_list()

    def file_write(self):
        bm = service.AIService()
        bm.save_list()