from class_exception import DuplicateException, RecordNotFoundException
from class_domain import AIEntity
import class_filestore

class AIService:
    #AIEntuty 정보를 저장하는 클래스 변수. 클래스 로드 시점에 초기화됨. 모든 클래스 멤버에서 공유.
    ai_list = []

    def register(self, ai_entity):
        idx = self.is_exist(ai_entity.email)
        if idx<0:
            AIService.ai_list.append(ai_entity) #클래스변수니까 self말고 클래스를 붙일 수 있음.
            return ai_entity.name+"님 등록되었습니다."
        else:
            try:
                raise DuplicateException(ai_entity.name)
            except DuplicateException as error:
                return str(error)

    #수강생 목록
    def get_all_entity(self):
        return AIService.ai_list

    #수강생 정보 수정
    def entity_update(self, ai_entity):
        idx = self.is_exist(ai_entity.email)
        if idx>=0:
            ai = AIService.ai_list[idx]
            ai.name = ai_entity.name
            ai.age = ai_entity.age
            ai.major = ai_entity.major
            return ai_entity.name+"님 정보 수정 되었습니다."
        else:
            try:
                raise RecordNotFoundException(ai_entity.name)
            except RecordNotFoundException as error:
                return str(error)

    #수강생 정보 삭제
    def entity_remove(self, email):
        idx = self.is_exist(email)
        if idx>=0:
            AIService.ai_list.remove(idx)
            return email+"님 정보 삭제되었습니다."
        else:
            try:
                raise RecordNotFoundException(email)
            except RecordNotFoundException as error:
                return str(error)

    #수강생 상세정보
    def get_ai_entity(self, email):
        for i in enumerate(AIService.ai_list):
            if i.email == email:
                return i
            else:
                return None
        # try:
        #     raise RecordNotFoundException(email)
        # except RecordNotFoundException as error:
        #     return str(error)

    #email 존재여부
    def is_exist(self, email):
        for idx, entity in enumerate(AIService.ai_list):
            if entity.email == email:
                return idx
        return -1

    def save_list(self):
        class_filestore.save_data(AIService.ai_list)

    def read_list(self):
        AIService.ai_list = class_filestore.read_data()