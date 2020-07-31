import sys
import GUI_windows
import PyQt5.QtWidgets as qtw

if __name__ == "__main__":
    # sys,argv 값은 현재 소스코드에 대한 절대 경로를 나타낸다. 즉, 현재 파일이름.py의 절대 경로를 나타낸다.
    # QApplication클래스의 인스턴스를 생성할 떄 생성자로 이 값(절대경로)을 전달해야 한다.
    # app이라는 이름의 qt 객체 생성. 애플리케이션 내에 반드시 하나만 존재해야 한다.

    app = qtw.QApplication(sys.argv)
    mywindow = GUI_windows.MyWindow()
    mywindow.show()

    app.exec_()