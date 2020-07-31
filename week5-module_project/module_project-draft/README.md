## 도커 설치
### docker toolbox
```
Running pre-create checks...
Error with pre-create check: "This computer doesn't have VT-X/AMD-v enabled. Enabling it in the BIOS is mandatory"
Looks like something went wrong in step ´Checking if machine default exists´... Press any key to continue...
```
* 위 오류를 해결하지 못하였다.
* 가상화 기능 enabled, 코어 격리 기능 off, hyper-V 비활성화 상태.

### docker desktop
* docker toolbox가 작동하지 않아서 docker desktop 설치. hyper-V를 활성화 하였으나 hyper-V 어쩌구 에러가 떠서 빡쳐있다가 갑자기 되었다. 컴퓨터가 구져서 반영되는데에 시간이 오래 걸리는 듯.
* hyper-V on/off
    - cmd 관리자 모드
    - bcdedit
    - 가장 아랫줄의 hyperv 어쩌구가 auto이면 on, off이면 off
* 제어판 - 프로그램 기능 켜기/끄기 에서도 가능.

### 에러 목록
* hyper-V 비활성화 시키기
    ```
    Raw-mode is unavailable courtesy of Hyper-V. (VERR_SUPDRV_NO_RAW_MODE_HYPER_V_ROOT).
    ```
    - docker toolbox 사용 시에는 hyper-V를 꺼야 한다.
    - cmd 관리자 모드
    - bcdedit
    - 가장 아랫줄의 hyperv 어쩌구가 auto일 때 off시키기
    ```
    bcdedit /set hypervisorlaunchtype off
    ```
    * *제어판 - 프로그램 기능 켜기/끄기 에서도 가능.

## docker로 mysql container 만들기
* [참고자료](https://velog.io/@wimes/Docker%EB%A1%9C-MySQL-%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88-%EB%A7%8C%EB%93%A4%EA%B8%B0)
1. 모든 도커 컨테이너&이미지 삭제
    ```
    docker system prune
    ```
2. Mysql 컨테이너 생성
    ```
    docker run -d -p 9876:3306 -e MYSQL_ROOT_PASSWORD=1234 mysql:5.7
    ```
    * ![image](https://user-images.githubusercontent.com/53554014/88922796-9ccad300-d2ab-11ea-9ffd-a52998cad25a.png)
    * mysql은 Dockerhub에 있기 때문에 즉시 image를 띄워볼 수 있다.
    * 비밀번호는 1234로 설정하였음.
    * 이미지를 pull한 후 컨테이너를 생성한 과정이 아니기 때문에 컨테이너 이름은 자동으로 할당되었음.
3. 컨테이너 정보 확인
    ```
    docker ps
    ```
    * NAMES=funny_albattani
4. mysql 컨테이너에 접속하여 bash로 실행
    ```
    docker exec -it funny_albattani
    ```
    * ![image](https://user-images.githubusercontent.com/53554014/88923423-ac96e700-d2ac-11ea-88f8-b0b475b59fb9.png)
5. mysql 명령 사용
    ```
    mysql -u root -p
    ```
    * ![image](https://user-images.githubusercontent.com/53554014/88923839-48c0ee00-d2ad-11ea-8fc5-8ff01fdf34d9.png)
6. mysql에서 DB 생성 및 확인
    ```
    mysql> CREATE DATABASE TEST;
    Query OK, 1 row affected (0.00 sec)

    mysql> SHOW DATABASES;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | TEST               |
    | mysql              |
    | performance_schema |
    | sys                |
    +--------------------+
    5 rows in set (0.00 sec)
    ```
7. container 세부정보 보기
    ```
    exit
    docker ps -a
    docker inspect funny_albattani
    ```
    * container ID로 확인할 수도 있고, names로 확인할 수도 있다.
    * ![image](https://user-images.githubusercontent.com/53554014/88924720-9853e980-d2ae-11ea-89da-32dc5cbf1e91.png)

***

## mysql 실행 정보
* mysql version = 5.7
* ip = 172.17.0.2
* 호스트 포트 = 9876
* 게스트 포트 = 3306
* 컨테이너 이름 = funny_albattani
* password = 1234

## 관리자 유저 생성 후 외부 접속
* admin user 생성
    * user = admin_test1
    * password = 1234
    ```
    mysql> use mysql
    mysql> CREATE USER 'admin_test1'@'%' IDENTIFIED BY '1234';
    ```
* 외부 접속 권한 부여
    ```
    mysql> GRANT ALL PRIVILEGES ON *.* TO 'admin_test1'@'%';
    ```
    * 이후 재시작하기
    ```
    $ docker restart funny_albattani
    ```
* 외부 접속 : heidiSQL(for windows)
    - 하이디SQL: SQL front이다. 설정한 container 정보를 입력한다.
    - username = admin_test1
    - password = 1234
    - port = 9876
    - host ip = 172.17.0.2
* heidiSQL을 이용한 쿼리 날리기
    - ![image](https://user-images.githubusercontent.com/53554014/88929204-c3d9d280-d2b4-11ea-98f5-c5fb3144213f.png)
    - 쿼리 작성 후 **F9** 키를 누르면 결과 반환.

***

## PyMySQL
```
pip install PyMySQL
```
* mysql db를 지원하는 파이썬 모듈 중 하나.

***

## DBschema
```
Club_
  |- clubID (primary key)
  |- clubName
  |- foundationDate
```
```
Membership_
  |- membershipID (primary key)
  |- clubID
  |- memberEmail
  |- role
  |- joinDate
```
```
Member_
  |- email (primary key)
  |- nickName
  |- phoneNumber
  |- birthday
```
* ![image](https://user-images.githubusercontent.com/53554014/88935727-043d4e80-d2bd-11ea-9e23-b29d1eaff75a.png)
* ![image](https://user-images.githubusercontent.com/53554014/88935865-2b941b80-d2bd-11ea-850d-e662a91a4aad.png)
    * 편의상 문자열 입력으로만 받는다.
```
mysql> desc Club_;
+----------------+-------------+------+-----+---------+-------+
| Field          | Type        | Null | Key | Default | Extra |
+----------------+-------------+------+-----+---------+-------+
| clubID         | varchar(50) | NO   | PRI | NULL    |       |
| clubName       | varchar(50) | YES  |     | NULL    |       |
| foundationDate | varchar(8)  | YES  |     | NULL    |       |
+----------------+-------------+------+-----+---------+-------+

mysql> desc Member_;
+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| email       | varchar(30) | YES  |     | NULL    |       |
| nickName    | varchar(30) | YES  |     | NULL    |       |
| phoneNumber | varchar(11) | YES  |     | NULL    |       |
| birthday    | varchar(8)  | YES  |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+

mysql> desc Membership_;
+--------------+-------------+------+-----+---------+-------+
| Field        | Type        | Null | Key | Default | Extra |
+--------------+-------------+------+-----+---------+-------+
| membershipID | varchar(50) | NO   | PRI | NULL    |       |
| clubID       | varchar(50) | YES  |     | NULL    |       |
| memberEmail  | varchar(50) | YES  |     | NULL    |       |
| role         | varchar(50) | YES  |     | NULL    |       |
| joinDate     | varchar(20) | YES  |     | NULL    |       |
+--------------+-------------+------+-----+---------+-------+
```

***

## mysql
* [SQL Tutorial](https://www.w3schools.com/sql/sql_insert_into_select.asp)
* [참고자료: 테이블 선언](https://www.everdevel.com/MySQL/creating-table/)
* [참고자료: 테이블 선언2](https://opentutorials.org/course/195/1537)
* **[참고자료: SQL과 파이썬](https://yurimkoo.github.io/python/2019/09/14/connect-db-with-python.html)**
* TEST 라는 이름의 DB 사용 선언
    ```
    mysql> use TEST
    ```
* 테이블 생성
    ```
    create table 테이블명(
        필드명 타입,
        필드명 타입
    );
    ```
* 테이블 확인, 테이블 내용 확인
    ```
    mysql> show tables;
    mysql> desc 테이블명;
    ```
* 필드 추가, 삭제, 수정
    - add, drop, change
    ```
    alter table 테이블명 add 추가할필드명 타입 after 기존필드이름뒤에추가;
    ```
* 필드 타입변경
    ```
    alter table 테이블명 modify 기존필드명 새로운타입;
    ```
* 테이블 이름변경
    ```
    alter table 기존테이블이름 rename 새테이블이름
    ```
* 데이터 삽입, 변경, 삭제
    - INSERT
    ```
    sql = '''INSERT INTO 테이블이름 (필드1, 필드2, 필드3) VALUES ("값1", "값2", "값3");'''
    cursor.execute(sql)
    DB이름.commit()
    ```
    - execute(): INSERT 쿼리 실행
    - commit(): 커밋을 날리지 않으면 execute()를 아무리 해도 결과가 DB에 반영되지 않음.
    - 
    - UPDATE
    ```
    sql = '''UPDATE 테이블이름 SET 필드1 = '값1' WHERE 변경할데이터;'''
    ```
    - WHERE절에는 primary key 등을 통해 명시적인 데이터를 이용하는 것이 안전하다.
* 데이터 조회
    - SELECT
    - execute()를 사용하여 sql을 실행한 후, fech 계열의 메서드를 이용해 실행한 결과를 받아온다.
    ```
    fetchall() | 모든 데이터를 한 번에 가져올 때 사용
    fetchone() | 한 번 호출에 하나의 행만 가져올 때 사용
    fetchmany(n) | n개만큼의 데이터를 가져올 때 사용
    ```
* Placeholder를 사용하여 execute하기
    - DB 내 데이터에 대량 삽입/변경/삭제가 필요한데, 조건이 다 다르다면?
    - Placeholder: 동적 SQL문을 구성할 때 사용하는 기능.
        - 동적 값이 들어갈 위치에 %s를 사용하여 SQL문을 만든다.
        - execute(sql문, 실제 데이터)
        - 실제 데이터는 리스트나 튜플 형태로 넣는다.
    - 특징
        - 두 번째 파라미터에 들어간 데이터 순서대로 SQL 적용됨.
        - 문자열의 경우 특수문자들이 자동으로 Escape
        - 문자열, 숫자 등에 관계없이 모두 %s

***

## GUI
```
pip install PyQt5
```