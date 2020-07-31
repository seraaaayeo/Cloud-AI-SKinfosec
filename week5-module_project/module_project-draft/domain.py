class ClubEntity:
    # 생성자 정의: 멤버변수 - clubID, name, foundationDate
    def __init__(self, clubID, clubName, foundationDate):
        self.clubID = clubID
        self.clubName = clubName
        self.foundationDate = foundationDate

    def __str__(self):
        return (f"{self.clubID} : {self.clubName} : {self.foundationDate}")


class ClubMembershipEntity:
    # 생성자 정의: 멤버변수 - uid, email, name, role, joinDate
    def __init__(self, membershipID, clubID, memberEmail, name_, role, joinDate):
        self.membershipID = membershipID
        self.clubID = clubID
        self.memberEmail = memberEmail
        self.role = role
        self.joinDate = joinDate
    
    # Overriding: email 정보가 같은 경우 같은 객체로 재정의
    def __eq__(self, email):
        if(self.email == email):
            return True
        else:
            return False

    def __str__(self):
        return (f"{self.membershipID} : {self.email} : {self.name_} : {self.role} : {self.joinDate}")


class MemberEntity:
    # 생성자 정의: 멤버변수 - email, nickName, phoneNumber, birthday
    def __init__(self, email, nickName, phoneNumber, birthday):
        self.email = email
        self.nickName = nickName
        self.phoneNumber = phoneNumber
        self.birthday = birthday
    
    # Overriding: email 정보가 같은 경우 같은 객체로 재정의
    def __eq__(self, email):
        if(self.email == email):
            return True
        else:
            return False

    def __str__(self):
        return (f"{self.email} : {self.nickName} : {self.phoneNumber} : {self.birthday}")


class AddressEntity:
    # 생성자 정의: 멤버변수 zipCode, zipAddress, streetAddress, country
    def __init__(self, zipCode, zipAddress, streetAddreess, country):
        self.zipCode = zipCode
        self.zipAddress = zipAddress
        self.streetAddress = streetAddreess
        self.country = country
    
    def __str__(self):
        return (f"{self.zipCode} : {self.zipAddress} : {self.streetAddress} : {self.country}")