def qsort(arr):
    '''
    기본 단계 : 원소의 개수가 0이거나 1인 배열
    '''
    small = []
    big = []
    if len(arr)<2:
        return arr
    else:
        '''
        재귀 단계
        '''
        pivot = arr[0]
        for i in arr[1:]:
            if i <= pivot:
                small.append(i)
            else:
                big.append(i)
    return qsort(small) + [pivot] + qsort(big)

print(qsort([10, 5, 2, 3]))
'''
* 주의 : pivot을 선택하는 방법에 따라 최악의 경우(O(n^2))이 나오기도 함.
* pivot을 선택하는 방법 -> ??
'''