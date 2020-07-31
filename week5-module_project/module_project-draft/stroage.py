'''
@function
데이터 저장

@stack
centos7/mysql, docker container
'''
import pymysql

class DBAccess:
    connection = None
    def __init__(self):
        DBAccess.connection = pymysql.connect(host='172.17.0.2',
        port='9876'
        user='test_admin1',
        password='1234',
        db='test',
        charset='uft8',
        cursor=pymysql.cursors.DictCursor #db와 상호작용하기 위해 생성하는 객체. DictCursor는 딕셔너리 형태로 결과를 반환해줌. 일반 cursor는 튜플 형태로 리턴.
        )
    
    def close(self):
        DBAccess.connection.close()

    def insert(self, entity, table_name):
        with DBAccess.connection.cursor() as cursor:
            if(table_name == 'Club_'):
                sql = "INSERT INTO Club_ (clubID, clubName, foundationDate) VALUES (%s, %s, %s)"
                cursor.execute(sql, (entity.clubID, entity.clubName, entity.foundationDate))
            elif(table_name == 'Member_'):
                sql = "INSERT INTO Member_ (email, nickName, phoneNumber, birthday) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (entity.email, entity.nickName, entity.phoneNumber, entity.birthday))
            elif(table_name == 'Membership_'):
                sql = "INSERT INTO MembershipList_ (membershipID, clubID, memberEmail, role, joinDate) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (entity.membershipID, entity.clubID, entity.memberEmail, entity.role, entity.joinDate))
            
            DBAccess.connection.commit() #커밋을 날리지 않으면 execute()를 아무리 해도 결과가 DB에 반영되지 않음.

    def update(self, entity, table_name):
        with DBAccess.connection.cursor() as cursor:
            if(table_name == 'Club_'):
                sql = "UPDATE Club_ SET clubName = %s, foundationDate = %s WHERE clubID = %s"
                cursor.execute(sql, (entity.clubName, entity.foundationDate, entity.clubID))
            elif(table_name == 'Member_'):
                sql = "UPDATE Member_ SET nickName = %s, phoneNumber = %s, birthday = %s WHERE email = %s"
                cursor.execute(sql, (entity.nickName, entity.phoneNumber, entity.birthday, entity.email))
            elif(table_name == 'Membership_'):
                sql = "UPDATE Membership_ SET clubID = %s, memberEmail = %s, role = %s, joinDate = %s WHERE membershipID = %s"
                cursor.execute(sql, (entity.clubID, entity.memberEmail, entity.role, entity.joinDate, entity.membershipID))
            
            DBAccess.connection.commit()
    
    def delete(self, delID, table_name):
        with DBAccess.connection.cursor() as cursor:
            if(table_name == 'Club_'):
                sql = "DELETE FROM Club_ WHERE clubID = %s"
                cursor.execute(sql, (delID))
            elif(table_name == 'Member_'):
                sql = "DELETE FROM Member_ WHERE email = %s"
                cursor.execute(sql, (delID))
            elif(table_name == 'Membership_'):
                sql = "DELETE FROM Membership_ WHERE membershipID = %s"
                cursor.execute(sql, (delID))
            
            DBAccess.connection.commit()

    def select_by_ID(self, ID, table_name):
        with DBAccess.connection.cursor() as cursor:
            if(table_name == 'Club_'):
                sql = "SELECT * FROM Club_ WHERE clubID = %s"
                cursor.execute(sql, (ID))
            elif(table_name == 'Member_'):
                sql = "SELECT * FROM Member_ WHERE email = %s"
                cursor.execute(sql, (ID))
            elif(table_name == 'Membership_'):
                sql = "SELECT * FROM Membership_ WHERE membershipID = %s"
                cursor.execute(sql, (ID))
            
            result = cursor.fetchone()
        return result

    

