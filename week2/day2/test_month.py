import datetime

def solution(a, b):
    answer = ''
    date = ["WED", "THU", "FRI", "SAT", "SUN", "MON", "TUE"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(0, a-1):
        total += month[i]
    answer = date[(total+b)%7 -1]
    
    return answer

def main():
    today = datetime.datetime.now()

    temp = str(today).split(" ")
    temp = temp[0]
    temp = temp.split("-")
    
    month = int(temp[1])
    date = int(temp[2])
    print("{}월 {}일은 {} 입니다.".format(month, date, solution(month, date)))

# def main():
#     today = datetime.datetime.now()
#     print(today)
#     print(today.month)

#     if today.month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
#         print("이번 달은 31일 까지 있습니다.")
#     elif today.month == 4 or 6 or 9 or 11:
#         print("이번 달은 30일까지 있습니다.")
#     elif today.month ==2:
#         print("28 일까지")
#     else:
#         print("error")


if __name__ == "__main__":
    main()