# 파일 한줄씩 출력하기
def print_lines(filename):
    line_number = 1
    with open('filename.txt') as file:
        for line in file:
            print(line_number, line)

# 단어의 빈도수로 단어 정렬
pairs = [('time', 8),
('the', 15)],
('turbo', 1)
def get_freq(pair):
    return pair[1]
def sort_by_freq(pairs): #(단어, 빈도수) 튜플의 리스트를 받아 정렬하여 리턴
    return sorted(pairs, key=get_freq)

# CSV 데이터 읽고 처리하기
import csv
def print_book_info(filename):
    with open(filename) as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            title = row[0]
            author = row[1]
            pages = row[3]
            print("{} ({}): {}p".format(title, author, pages))

def main():
    filename = 'books.csv'
    print_book_info(filename)

if __name__ == "__main__":
    main()