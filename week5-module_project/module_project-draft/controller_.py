'''
@function
View에서 요청하는 데이터의 유효성 체크
'''

import service

class VaildDataCheck:
    def register_controller(self, IDcode, entity, table_name):

        if IDcode == "" or IDcode == 0 : 
            return "ID코드 형식이 잘못됐습니다."
        else:
            bm = service.CommunityService()
            message = bm.register(entity, table_name)
            return message

    def get_all_entity_controller(self, table_name, ID_, key_name):
        bm = service.CommunityService()
        list_ = bm.get_all_entity(table_name, ID_, key_name)
        return list_

    def update_controller(self, IDcode, entity, table_name):
        if IDcode == "" or IDcode == 0 :
            return "ID코드 형식이 잘못됐습니다."
        else:
            bm = service.CommunityService()
            message = bm.entity_update(entity, table_name)
            return message
    
    def delete_controller(self, IDcode, table_name):
        if IDcode == "" or IDcode == 0 :
            return "ID코드 형식이 잘못됐습니다." 
        else:
            bm =service.CommunityService()
            message = bm.entity_remove(IDcode, table_name)
            return message 

    def close(self):
        bm=service.CommunityService()
        bm.close()
