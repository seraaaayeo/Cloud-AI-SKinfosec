# TIL: 2020-07-10

## 예외처리
* try-except
    - try: 예외가 발생할 가능성이 있는 구문
    - except : 예외가 발생했을 때 실행할 구문
    - finally
    - else
* Multi-exception handiling
    - as 키워드 사용.
    - Exception(부모타입), Value Error 등등(자식 타입)
    - 상속되는 예외를 처리할 때 자식타입 예외를 먼저 처리해야 함.

## 표준 모듈
* package = directory처럼 모듈이 모인 구조.
    - main.py는 엔트리 포인트로, test_package 폴더(디렉터리)는 패키지로 사용
* import = path 잡기
* sys 모듈
    - exit()의 경우에는 sys를 import하지 않아도 사용할 수 있음.
    ```
    sys.exit()
    exit()
    ```
## Event 처리
* 데코레이터

## 외부 모듈
* BeautifulSoup
    - 주말에 크롤링 복습을 하자.
* Flask
* 라이브러리
* 프레임워크

## 모듈화
* 여러 모듈 중 실행할 모듈을 엔트리 포인트로 잡기.
    - ex.make_cal.py와 use_cal.py 모듈이 있을 때 use_cal.py를 엔트리 포인트로 잡는다.
    - make_cal.py 모듈은 엔트리 포인트에서 import한다.

## Class
* __eq__와 같은 메소드는 여러 모듈에서 사용할 수 있다.
    - 최상위 class에서 정의되었기 때문.

## Arcitecture Pattern : Tier와 Layer
* Layer: UI - Presentation - Service - Data Access (컴네를 생각해보자)
* Tier : 
    - DB는 연구실 컴을 쓰고 웹서버는 집컴을 쓰기로 했다. 프론트는 노트북에서 구현한다. ->Tier가 UI, DB, Service로 나눠짐.

***

## 실습
* 

***

## 혼자서 공부한것
### Generator
* list 와 generator 성능 비교 : 백만명의 학생 정보가 들어가는 리스트 생성
    - list : 
        - 시작 전 메모리 사용량: 12.125MB
        - 종료 후 메모리 사용량: 13.65625MB
        - 총 소요된 시간: 1.375000 초
    - generator :
        - 시작 전 메모리 사용량: 12.17578125MB
        - 종료 후 메모리 사용량: 12.18359375MB
        - 총 소요된 시간: 0.000000 초

### Mecab 설치
* Trouble shooting : 버전 문제
    - Python3.8의 하위폴더 site-package에 3.7버전 python wheel을 설치하여 버전 문제 발생.
    - cmd, vscode terminal에서 python wheel 설치 안 됨. anaconda prompt에서 설치해야 됨.
    - anaconda는 3.7버전이므로 아나콘다 Lib/site-package에 python wheel을 설치하면 됨.
* Mecab을 설치하기 위해 고군분투중에 있다. 
    - 설치를 하긴 했는데 Mecab()이거가 안 돼서 찾아보니까 여러가지를 설치 해야 하는 것 같다...
* eunjeon 패키지를 설치하여 해결하였다. C++로 빌드해야 되는데 visual studio가 없어서 에러가 나길래 깔아줬다.
* 권한 에러가 나길래 에러로그 보고 --user 태그를 붙여주었다.(관리자 권한으로 anaconda prompt를 실행해도 에러가 났음.)

### Word cloud 한국어 decoding
