'''
클래스가 할당하는 시점 테스트
'''
class Count:
    staticCount = 0

    def __init__(self, cnt):
        self.cnt = cnt

'''
클래스 초기화 시점
'''
c1 = Count(0)
c2 = Count(0)
print(Count.staticCount) #0
print(c1.staticCount) #0

'''
클래스 이름으로 참조할 경우
'''
Count.staticCount = c1.staticCount + 1
print(c1.staticCount) #1
Count.staticCount = c2.staticCount + 1
print(c2.staticCount) #2
print("클래스 이름으로 참조", c1.staticCount, c2.staticCount) # 2 2

'''
인스턴스로 참조할 경우
클래스를 객체처럼 참조할 때 마다 초기화하여 할당한다.
'''
c1.cnt = c1.cnt + 1
print(c1.cnt) #1
c2.cnt = c2.cnt +1
print(c2.cnt) #1
print("인스턴스로 참조", c1.cnt, c2.cnt) #1 1
