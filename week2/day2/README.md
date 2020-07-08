# TIL : 2020-07-07

## 파이썬 기초 문법을 배웠음.
* format
    ```
    format_a = "{}만 원".format(5000)
    print(format_a)  #5000만 원

    format_b = "{} {}".format(1000, 5000)
    print(format_b)  #1000 5000

    format_c = "{:5f}".format(52.273)
    print(format_c)  #52.27300
    ```

* datetime
    ```
    import datetime
    
    today = datetime.datetime.now() #현재 시간 반환
    month = today.month #현재 월 반환
    date = today.day #현재 일 반환
    ```
    - datetime.datetime.now().hour
    - datetime.datetime.now().min
    - 현재 연, 월, 일, 시, 분, 초 반환 가능

* lower, upper, rstrip, isdigit, isalpha, find 등.
* 이외에도 if문 등 기본 문법을 배웠음.
* syntax error, value error, type error 등도 배웠음.

## 간단한 자료구조를 배웠음.
* 리스트

## 실습
* datetime