# Multi Exception 처리
def multi_exception():
    list_data = [10,20,30]
    try:
        int_data = int(input("정수형 데이터 입력: "))
        list_data.append(int_data)
        for index in range(len(list_data)+1):
            divide_sum = list_data[index]+list_data[index] / (index+1)
            print(f"{index+1}번째 데이터: {list_data[index]}")
    except ValueError:
        print("Value Error: 정수형 데이터를 입력하")
    except IndexError:
        print(f"IndexError: 데이터 접근은 0~{len(list_data)-1}")
    except Exception as error:
        print(error, "프로그램에 무눈제가 이어서 종ㅇ료(")
    
def main():
    multi_exception()

if __name__== "__main__":
    main()