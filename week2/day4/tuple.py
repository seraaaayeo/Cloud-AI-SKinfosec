# 튜플 선언 방법
def printTup(data1, data2):
    print(type(data1)) #<class 'tuple'>
    print(type(data2)) #<class 'tuple'>

# 튜플을 이용한 값 교환
def swap(a, b):
    a, b = b, a
    print(a, b)

# 람다 연습
def ori(n):
    ans = 0
    for i in range(1, n+1):
        if(n%i == 0):
            ans +=i
    return ans
def oneline(n):
    return sum([i for i in range(1, n+1) if n%i==0])
def testLambda(n):
    print(list(filter(lambda i: n%i==0, range(1, n+1))))
    return sum(filter(lambda i: n%i==0, range(1, n+1)))

# 일급함수: 함수의 매개변수로 함수 전달하기
def increase(val, ori):
    return ori+val
def decrease(val, ori):
    return ori-val
def change_data(func, change_data, ori_list):
    for idx, ori_data in enumerate(ori_list):
        ori_list[idx] = func(change_data, ori_data)
    print(f"changed data: {ori_list}")

#  map 사용
def m_increase(val):
    return val+10
def m_decrease(val):
    return val-10
def m_change_data(func, ori_list):
    new_list=[]
    for idx, val in enumerate(ori_list):
        new_list.append(func(val))
    return new_list


###########
def main():
    # Tuple
    data1 = (10, 20, 30)
    data2 = 10, 20, 30
    printTup(data1, data2)
    
    # Swap with tuple
    swap(10, 20)

    # Test lambda
    print(ori(15))
    print(oneline(15))
    print(testLambda(15))

    # Scream data
    ori_list = [10,20,30,40,50]
    change_data(increase, 10, ori_list)
    change_data(decrease, 5, ori_list)

    # Scream data fixed to map
    print(f"new list: {m_change_data(m_increase, ori_list)}")
    print(f"new list: {m_change_data(m_decrease, ori_list)}")

    # Scream data with map
    out_increase = map(m_increase, ori_list)
    print(f"map: {list(out_increase)}")
    out_decrease = map(m_decrease, ori_list)
    print(f"map: {list(out_decrease)}")

    # Scream data with lambda
    print(f"lambda: {list(map(lambda val: val+10, ori_list))}")
    print(f"lambda: {list(map(lambda val: val-10, ori_list))}")


if __name__ == "__main__":
    main()