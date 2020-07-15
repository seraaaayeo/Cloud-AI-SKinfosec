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
    docker image prune //사용하지 않는 이미지 삭제
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
    - 표준 입출력을 가지고 사용할 것이다.
    ```
    docker run --interactive --tty
    docker run -it 
    ```
    - ![image](https://user-images.githubusercontent.com/53554014/87495420-5ad74580-c68c-11ea-9667-663a1149b010.png)
    ```
    docker run -it --name centos_cal centos:7 /bin/cal
    ```

***

## 실습
* 

***

## 혼자서 공부한 것
### Docker
* [참고 자료](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)
* 컨테이너 기반의 오픈소스 가상화 플랫폼.


