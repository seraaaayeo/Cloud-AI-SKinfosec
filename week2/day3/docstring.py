class DocstringClassExample():
    """
    Docstring 예제 클래스
    class에 대한 설명을 함께 적는다.
    """

    def docstringFuncExample(self):
        """
        Docstring 예제 함수
        Return 0 always
        """
        print("함수를 실행하였습니다.")
        return 0

def main():
    print("Docstring 실습")
    
    new_doc = DocstringClassExample()
    print("Class docstring start")
    print(new_doc.__doc__)
    print("Class docstring end")

    print("Function docstring start")
    print(new_doc.docstringFuncExample.__doc__)
    print("Function docstring end")

if __name__ == '__main__':
    main()