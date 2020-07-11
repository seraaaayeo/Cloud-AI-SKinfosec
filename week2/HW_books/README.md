# HW: 2020-07-11

## Description
* 1주차 과제: 도서 관리 시스템
* 요구사항
    - 모듈화
    - View, controller, model의 architecture pattern을 따를 것.

## How to run
```
cd your\path\week2\HW_books
python view.py
```
Or you can just run python file including path
```
python \week2\HW_books\view.py
```

## Architecture
* [View](https://github.com/seraaaayeo/Cloud-AI-SKinfosec/blob/master/week2/HW_books/view.py): DB에서 받아온 data를 출력
* Controller: View의 요청이 있을 때 DB에 접근하여 데이터를 업데이트하거나 데이터를 받아옴.
    - CRUD 요청
    - [신규 도서 데이터 생성](https://github.com/seraaaayeo/Cloud-AI-SKinfosec/blob/master/week2/HW_books/create.py)
    - [요청에 따른 데이터 읽어오기](https://github.com/seraaaayeo/Cloud-AI-SKinfosec/blob/master/week2/HW_books/read.py)
    - [데이터 업데이트](https://github.com/seraaaayeo/Cloud-AI-SKinfosec/blob/master/week2/HW_books/update.py)
    - [데이터 삭제](https://github.com/seraaaayeo/Cloud-AI-SKinfosec/blob/master/week2/HW_books/delete.py)
* Model: 직접적으로 데이터를 저장하는 DB의 역할.
    - 파일 입출력을 통한 데이터 저장
    - [데이터 입력](https://github.com/seraaaayeo/Cloud-AI-SKinfosec/blob/master/week2/HW_books/data_in.py)
    - [데이터 출력](https://github.com/seraaaayeo/Cloud-AI-SKinfosec/blob/master/week2/HW_books/data_out.py)
