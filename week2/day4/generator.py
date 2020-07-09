def square_nums(nums):
    res= []
    for i in nums:
        res.append(i*i)
    return res

def generator_square_nums(nums):
    for i in nums:
        yield i*i

def main():
    '''
    일반적으로 함수 정의 및 호출 방법.
    '''
    nums = square_nums([1, 2, 3, 4, 5])
    print(nums)

    '''
    Generator : 제너레이터라는 오브젝트 반환.
    generator는 자신이 리턴할 모든 값을 메모리에 저장하지 않고, 한 번 호출될 때마다 하나의 값만을 전달(yield)
    '''
    gen_nums = generator_square_nums([1, 2, 3, 4, 5])
    print(gen_nums) # <generator object generator_square_nums at 0x031BA568>
    # print(next(gen_nums)) #1
    # print(next(gen_nums)) #4
    # print(next(gen_nums)) #9
    # print(next(gen_nums)) #16
    # print(next(gen_nums)) #25
    # print(next(gen_nums)) #StopIteration (예외 발생)

    for num in gen_nums:
        print(num)


if __name__ == "__main__":
    main()
    