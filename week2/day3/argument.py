# Argument and Parameter
def func1(param1, param2):
    '''
    func1에는 매개변수 param1, param2가 전달받는다.
    매개변수: 함수가 정의되는 내용에 포함(Variable)
    '''
    print(f"parameter1: {param1}, parameter2: {param2}")

'''
func1에 "AA"와 "B"라는 값을 전달하며 함수를 호출한다.
인자: 함수에 전달하는 값(Value)
'''
func1("AA", "B") #parameter1: AA, parameter2: B

# 인자의 전달방식 - Call by Value & Call by Reference
def call_by_value(param1:int)->None:
    param1 +=1
    print(f"callb by value: {param1}")

def call_by_ref(param2:list)->None:
    param2[0]+=1
    print(f"call by ref: {param2}")

val1 = 3
val2 = [3]

print(f"ori val1:{val1}") #3
call_by_value(val1) #4
print(f"val1 after func:{val1}") #3
print("--------")
print(f"ori val2:{val2}") #[3]
call_by_ref(val2) #[4]
print(f"val2 after func:{val2}") #[4]
'''
call by value: 함수로 인자가 전달될 때 동일한 값을 가진 객체를 복사하여 전달.
 = val1이 전달된 것이 아니라 val1과 동이란 값을 가진 객체가 전달됨.
call by reference: 함수로 인자가 전달될 때 실제로 인자가 가진 참조 값을 전달.
 = 실제로 인자 객체를 그대로 전달.
'''
