# TIL: 2020-07-08

## 파이썬 기초 문법을 또 배웠음.
* 오늘은 for문
* dictionary = map
    - Map: key: value 자료구조 형태의 데이터.
    - JS object(JSON)이 이 형태의 데이터 포맷.
    - 다양한 언어에서 해당 자료구조 제공.
    - 따라서 파이썬에서도 Map 형태의 자료구조를 제공하기 위해 딕셔너리 등장.
    - 소켓통신, XML 이후에 등장. 값을 파싱하여 해석할 필요가 없이 simple하여 많이 쓰임.
    - json.org
* string notation: 
    - single quotation(') - 1 character
    - double quotation(") - more than two character
* Thread: 최소 작업 단위
* time: Unix time반환
    '''
    import time
    time.time()
    '''

## 실습
* for문으로 짝수만 출력하라해서 입력을 random함수로 바꿔봤음
* for문으로 구구단을 출력하였음

***

## 혼자서 공부한것
#### 문서화
* Docstring: 코드에 포함된 문서. 함수, 클래스 모듈 등에 정의할 수 있다.
* __doc__ : 작성한 문서를 확인 가능.

#### 인자 호출 방식
* call by value: 함수로 인자가 전달될 때 동일한 값을 가진 객체를 복사하여 전달.
 = val1이 전달된 것이 아니라 val1과 동이란 값을 가진 객체가 전달됨.
* call by reference: 함수로 인자가 전달될 때 실제로 인자가 가진 참조 값을 전달.
 = 실제로 인자 객체를 그대로 전달.
* 파이썬은 함수에 전달되는 인자의 타입에 의해 호출을 결정한다.
    * immutable 객체: int, float, str, tuples -> 값에 의한 호출
    * mutable 객체: list, set, dict -> 참조에 의한 호출

#### 가변 인자 함수
* 가변 인자 함수: 인자의 개수가 정해지지 않은 함수
* *args 와 같이 *를 이용한 매개변수는 가변인자를 받을 수 있는 것으로 해석된다.
* *를 사용하는 것을 packing한다고 표현하기도 한다.
