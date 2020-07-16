# TIL: 2020-07-14

## MySQL
* SQL: Structured Query Language
    - ![image](https://user-images.githubusercontent.com/53554014/87643100-5fcbf000-c785-11ea-822b-b10ddd4e7a79.png)
    - 개발자들이 DB쿼리를 쉽게 하기 위해 만든 표준.

***

## 실습
* Docker nginx 실습
    - pre-requists
        1. docker workspace 만들기
        2. vscode docker 확장파일 설치
        3. vitual box 실행
    - ubuntu_nginx
        1. Dockerfile 만들기
        2. 실행시킬 index.html 만들기
        3. 도커 이미지 빌드
        ```
        docker build -t unginxweb:1 . //.은 Dockerfile을 찾는 역할을 한다. -t 태그 옆에는 이름 지정
        ```
        4. 도커 이미지 생성 확인
        ```
        docker images
        ```
        5. 컨테이너 생성
        ```
        docker run --name unginxserver -d -p 80:80 unginxweb:1
        curl localhost //로컬호스트 확인. 인터넷에서 로컬호스트를 확인해도 됨.
        ```
        6. 컨테이너 확인
        ```
        docker ps
        ```
        7. 배쉬파일 실행
        ```
        docker exec -it unginxserver bash
        ```
        8. 배쉬에서 index.html 확인
        ```
        #ls -al /usr/share/nginx/html
        #cat /usr/share/nginx/html/index.html
        ```
        9. 배쉬에서 주소 이전
        ```
        #mv /usr/share/nginx/html/index.html /var/www/html
        ```
        10. 로컬호스트 확인
        ```
        curl localhost //http 메시지를 쉘 상에서 요청하여 결과를 확인하는 명령어. 이렇게 쓰면 GET 메소드를 사용하는 것이다.
        ```
* Docker mysql 실습
    1. 도커허브에서 mysql 이미지 가져오기
    ```
    docker pull mysql:5.7
    ```
    2. 컨테이너 생성
    ```
    docker run --name mysql5 -e MYSQL_ROOT_PASSWORD=1234 -d -p 3306:3306 mysql:5.7
    ```
    - -e: 인증
    - MYSQL_ROOT_PASSWORD: 바꿀 수 없는 상수, 반드시 등록되어야 하는 key
    3. 배쉬 실행
    ```
    docker exec -it mysql5 bash
    ```
    4. os 확인
    ```
    #cat /etc/issue //Debian GNU/Linux 10
    ```
    5. mysql 위치확인
    ```
    #whereis mysql
    ```
    - ![image](https://user-images.githubusercontent.com/53554014/87641791-90ab2580-c783-11ea-9b42-093c367469eb.png)
    6. mysql 명령 사용하기
    ```
    #mysql -u root -p
    ```
    - ![image](https://user-images.githubusercontent.com/53554014/87642351-5d1ccb00-c784-11ea-8046-e1cbb4362dbd.png)
    7. mysql 사용하기
    ```
    #use mysql
    ```
* [Query문 연습](https://www.w3schools.com/default.asp)
