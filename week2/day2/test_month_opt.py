# test_month 함수 최적화
# python의 datetime을 이용하면 연, 월, 일, 시, 분, 초 모두 출력 가능함.
# 2020년 1월 1일은 수요일이므로 date리스트는 수요일로 시작.
# 2020년 2월은 윤달.

import datetime

def solution(a, b):
    answer = ''
    date = ["수", "목", "금", "토", "일", "월", "화"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(0, a-1):
        total += month[i]
    answer = date[(total+b)%7 -1]
    
    return answer

def main():
    today = datetime.datetime.now()
    
    month = today.month
    date = today.day
    print("{}월 {}일은 {}요일입니다.".format(month, date, solution(month, date)))

if __name__ == "__main__":
    main()