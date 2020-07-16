# TIL: 2020-07-14

## Docker(container)
* kitematic은 cri명령어에 익숙치 않은 사람들을 위함(마치 깃허브 데스크탑처럼? cmake GUI처럼?). docker hub 로그인해야함.
* nginx
    - docker pull nginx
    - 포트포워딩을 통한 포트 변경
        - ![image](https://user-images.githubusercontent.com/53554014/87489769-cdd9bf80-c67e-11ea-9011-5b8fd648db41.png)
        - virtual box -> network -> 고급 설정 -> 포트포워딩 규칙
    ```
    docker run --name webserver -d -p 80:80 nginx
    ```
    - 이름은 webserver, 데몬 백그라운드(프로세스가 종료되지 않고 계속 실행), 포트는 80(host), 80(guest)으로 nginx를 run한다.
    - ![image](https://user-images.githubusercontent.com/53554014/87490517-d3d0a000-c680-11ea-81c7-8dd1a8bf4ad5.png)
    - localhost(http://localhost 혹은 http://localhost:80)에 nginx 서버가 표시됨.
* 도커 명령어
    - docker stop NAME : NAME이라는 이름의 컨테이너 중지
    - docker start NAME
    - docker rename NAME RENAME
    ```
    docker rename webserver web
    ```
    - docker rm, prune: Exited된 컨테이너 삭제. 이미지를 삭제할 때는 반드시 **컨테이너를 먼저 삭제**하고 이미지를 삭제해야 함.
    ```
    docker rm hello-world //name으로 지우기
    docker rm bf756fb1ae65 //ID로 지우기
    docker system prune //사용하지 않는 이미지 삭제
    docker rm -v //exit된 컨테이너를 한 번에 삭제
    ```
    - ![image](https://user-images.githubusercontent.com/53554014/87495915-75f68500-c68d-11ea-8a53-bd68a55e14cf.png)
    ```
    docker ps -a //컨테이너 확인
    docker rm containerName, docker container rm containerName //컨테이너 삭제
    docker ps -a //컨테이너가 지워졌는지 확인
    docker images //이미지 확인
    docker image rm imageID //이미지 삭제
    ```
    - docker image ls: pull한 이미지 확인
    - docker search imageName: 해당이름의 이미지 버전 등 정보 확인
    ```
    docker search centos
    ```
    - 이미지를 pull할 때 태그를 통해 버전을 다르게 받을 수 있다. 태그를 안 달 경우 default(latest) 이미지가 받아짐
    ```
    docker pull centos //default version
    docker pull centos:7(tag) //v7
    ```
    - 이미지 config 조회
    ```
    docker image inspect centos:7
    ```
    ```
    [
    {
        "Id": "sha256:b5b4d78bc90ccd15806443fb881e35b5ddba924e2f475c1071a38a3094c3081d",
        "RepoTags": [
            "centos:7"
        ],
        "RepoDigests": [
            "centos@sha256:e9ce0b76f29f942502facd849f3e468232492b259b9d9f076f71b392293f1582"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2020-05-05T21:20:07.182447994Z",
        "Container": "c171c5a1528a7b8dfc74e0fdf97920d6fc5dd3f13eb85fe52dcb4a0e0e5718d6",
        "ContainerConfig": {
            ...
        }
    }
    ]
    ```
    - centos의 /bin/cal -calendar실행
    - 표준 입출력을 가지고 사용할 것이다. 터미널 사용을 위한 명령어
    ```
    docker run --interactive --tty
    docker run -it 
    ```
    - ![image](https://user-images.githubusercontent.com/53554014/87495420-5ad74580-c68c-11ea-9667-663a1149b010.png)
    ```
    docker run -it --name centos_cal centos:7 /bin/cal
    ```
    - bash shell 사용하기
    - ![image](https://user-images.githubusercontent.com/53554014/87496872-611af100-c68f-11ea-8023-4ea69c0b1f77.png)
    ```
    docker run -it --name centos_shell centos:7 /bin/bash
    ```
    - ![image](https://user-images.githubusercontent.com/53554014/87497105-db4b7580-c68f-11ea-8425-036fd7a8a676.png)
    ```
    docker run -it --name ubuntu_shell ubuntu /bin/bash
    ```
    - chmod: 파일 권한 변경
    - 생성된 컨테이너로 들어가기
    - ![image](https://user-images.githubusercontent.com/53554014/87497503-a1c73a00-c690-11ea-8a1b-bd67ef6f97b0.png)
    ```
    docker start -i ubuntu_shell //시작
    ctrl+p+q //도커 프롬프트로 돌아오기. 우분투쉘 컨테이너는 실행 중(Up)
    docker attach ubuntu_shell //도커 프롬프트에서 실행 중인 우분투 터미널로 돌아가기
    ```
    - 컨테이너 아이디 반환
    ```
    docker ps -q //아이디 반환
    docker stop `docker ps -q` //up상태인 컨테이너 모두 자동 종료
    docker start `docker ps -a -q` //컨테이너를 모두 자동 시작
    ``` 
    - 도커 네트워크
    ```
    docker network ls
    docker network (container/image)    inspect ID //container를 확인할 경우 생략 가능, image는 추가해야 함.
    ```
* 쉘 스크립팅
    ```
    for index in `docker ps -q`;do docker stop $index;done
    ```
    - 돌아가고 있는 프로세스들을 차례대로 exit시킴.

* 우분투 명령어
    - su: 경로이동
    ```
    su root
    su user1
    ```
    - passwd: 패스워드 설정
    ```
    passwd root //루트 디렉터리 패스워드 설정
    ```
    - cat: 
    - ls -al: 파일권한 보기
    ```
    ls -al //모든 파일권한 보기
    ls -al /etc/shadow //해당 파일권한 보기
    ```
    - apt-get update
    - apt-get install sudo

* centos 명령어
    - yum install
    - yum install package_name -y : y태그를 붙일 경우 자동으로 yes 설정됨.

* vi 에디터
    ```
    yum update
    yum install vim
    vim test.txt
    ```
    - Enter: Insert mode
    - 한 번 더 엔터: 명령 mode
    - :wq 저장하고 종료
    - :qa / :q! 그냥 종료
    ```
    cat test.txt //텍스트 확인
    !vim //최근 텍스트파일 편집
    ```


***

## 실습
* 

***

## 혼자서 공부한 것
### Docker
* [참고 자료](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)
* 컨테이너 기반의 오픈소스 가상화 플랫폼.
* 컨테이너: 격리된 공간에서 프로세스가 동작하는 기술. 가상화 기술의 한 종류.
    - 기존의 가상화 방식
        - OS를 가상화(VM:Virtual Machine, Virtual Box)
        - 호스트 OS 위에 게스트 OS 전체를 가상화하여 사용한다.
        - ex.윈도우에서 리눅스 운영체제 사용 등.
    - 추가적인 OS를 설치하여 가상화하는 방법은 성능문제가 발생하기 때문에, 이를 개선하기 위해 프로세스를 격리하는 방식이 등장(container)
* 이미지: 컨테이터 실행에 필요한 파일과 설정값들을 포함하고 있는 것.
    - ex.우분투 이미지는 우분투를 실행하기 위한 모든 파일을 가지고 있고 MySQL 이미지는 debian을 기반으로 MySQL을 실행하는데 필요한 파일과 실행 명령어, 포트 정보 등을 포함.

### 정규 표현식
* [참고 자료(위키)](https://ko.wikipedia.org/wiki/%EC%A0%95%EA%B7%9C_%ED%91%9C%ED%98%84%EC%8B%9D)
