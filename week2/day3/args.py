# 가변 인자 함수: 인자의 개수가 정해지지 않은 함수
def arg_func1(a, b, c):
    print(f"a:{a}, b:{b}, c:{c}, sum:{a+b+c}")

def arg_func2(a, b, *args):
    print(f"a:{a}, b:{b}, args:{args}, sum:{a+b+sum(args)}")

print("test1")
arg_func1(1, 2, 3)
print("---------")
print("test2")
'''
args로 받은 인자는 튜플로 받아서 처리
'''
arg_func2(1, 2, 3) #a:1, b:2, args:(3,), sum:6
arg_func2(1, 2, 3, 4, 5, 6) #a:1, b:2, args:(3, 4, 5, 6), sum:21