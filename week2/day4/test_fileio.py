# text data 출력
def print_text_data():
    write_file = open("hello.txt", "w")
    write_file.write("Hello Python...")
    write_file.close()

# file 입력 -> console 출력
def print_console():
    with open("hello.txt", "r") as file:
        contents = file.read()
    print(contents)

# console 입력 -> file 출력
def read_file(filename, contents):
    with open(filename, "w") as file:
        file.write(contents)

# file 입력 -> file 출력(filecopy)
def rw_file(filename):
    with open(filename, "w") as file:
        file.write("Hello Python Modified....")

def main():
    print_text_data()
    #print_console()
    #read_file("hello.txt", "Hello Modified!")
    #rw_file("hello_modified.txt")

if __name__ == "__main__":
    main()