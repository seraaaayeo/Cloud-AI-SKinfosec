class AIEntity:
    # 생성자 정의: 멤버변수 - name, age, email, major
    def __init__(self, name, age, email, major):
        self.name = name
        self.age = age
        self.email = email
        self.major = major
    
    # Overriding: email 정보가 같은 경우 같은 객체로 재정의
    def __eq__(self, email):
        if(self.email == email):
            return True
        else:
            return False

    def __str__(self):
        return (f"{self.name} : {self.email} : {self.major}")
    
    '''
    toJson : Entity -> Json 변환
    fromJson : Json -> Entity 변환
    '''