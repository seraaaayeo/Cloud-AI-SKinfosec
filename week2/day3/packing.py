# packing
def packin_func(a, b, c):
    print(f"a:{a}, b:{b}, c:{c}, sum:{a+b+c}")

packing_list = [1, 2, 3]
#packin_func(packing_list) #error: 3개의 인자가 필요한 함수에 리스트 형태의 1개의 인자만 전달되었다.
packin_func(*packing_list) #a:1, b:2, c:3, sum:6