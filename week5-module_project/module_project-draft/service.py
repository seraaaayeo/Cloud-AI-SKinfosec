from exception import DuplicateException, NotFoundedException
from domain import ClubEntity, ClubMembershipEntity, MemberEntity
from stroage import DBAccess

def check_tableName(entity, tableName):
    if(tableName == 'Club_'):
        ID = entity.clubID
        name = entity.clubName
    elif(tableName == 'Member_'):
        ID = entity.email
        name = entity.nickName
    elif(tableName == 'Membership_'):
        ID = entity.membershipID
        name = entity.name_
    return (ID, name)

class ClubService:
    db = DBAccess()
    
    def close(self):
        ClubEntity.db.close()

    def is_exist(self, ID, table_name):
        result = ClubService.db.select_by_ID(ID, table_name)
        return result
        
    
    #Club Entity 등록: ID 중복여부 체크
    def register(self, entity, table_name):
        (ID, name) = check_tableName(entity, table_name)
        result = self.is_exist(ID, table_name)

        if not bool(result):
            ClubService.db.insert(entity, table_name)
            return str(name) + "이/가 등록되었습니다."
        else:
            try:
                raise DuplicateException(name)
            except DuplicateException as registError:
                return str(registError)
    
    #Entity 조회 기능 만들어야 함.
    #DB select로 정보 받아오기.

    #Entity 정보 수정
    def update(self, entity, table_name):
        (ID, name) = check_tableName(entity, table_name)
        result = self.is_exist(ID, table_name)

        if not bool(result):
            ClubService.db.update(entity, table_name)
            return str(name) + "의 정보가 수정되었습니다."
        else:
            try:
                raise NotFoundedException(name)
            except NotFoundedException as updateError:
                return str(updateError)

    #Entity 삭제
    def delete(self, entity, table_name):
        (ID, name) = check_tableName(entity, table_name)
        result = self.is_exist(ID, table_name)

        if not bool(result):
            ClubService.db.delete(ID, table_name)
            return str(ID) + "의 정보가 삭제되었습니다."
        else:
            try:
                raise NotFoundedException(ID)
            except NotFoundedException as deleteError:
                return str(deleteError)


        