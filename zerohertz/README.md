> Index

- [객체지향 프로래밍이란](#객체지향-프로래밍이란)
  - [예제로 알아보는 절차적 파이썬](#예제로-알아보는-절차적-파이썬)
  - [OOP로 물체 모델링하기](#oop로-물체-모델링하기)
  - [객체의 멘털 모델과 SELF의 의미](#객체의-멘털-모델과-self의-의미)
  - [여러 객체 관리](#여러-객체-관리)
- [파이게임과 GUI](#파이게임과-gui)
  - [파이게임 시작하기](#파이게임-시작하기)
  - [객체지향 파이게임](#객체지향-파이게임)
  - [파이게임의 GUI 위젯](#파이게임의-gui-위젯)
- [캡슐화, 다형성, 상속](#캡슐화-다형성-상속)
  - [캡슐화](#캡슐화)
  - [다형성](#다형성)
  - [상속](#상속)
  - [객체가 사용하는 메모리 관리](#객체가-사용하는-메모리-관리)
- [디자인 패턴과 마무리](#디자인-패턴과-마무리)

---

<!-- 1주차 -->

# 객체지향 프로래밍이란

## 예제로 알아보는 절차적 파이썬

+ 절차적 프로그래밍 (Procedural programming): 전체 프로그램을 여러 함수 (절차 또는 서브루틴)로 분할하는 기법
+ 객체지향 프로그래밍 (Object-Oriented Programming, OOP): 코드와 데이터를 결합하는 방식으로 절차적 프로그래밍에서 발생할 수 있는 복잡성 회피 가능

+ 절차적 프로그래밍이 겪은 공통 문제: 전역 데이터 사용 시 재사용의 어려움 (`global`)
  + 디버깅이나 유지보수의 어려움
  + 지나치게 많은 데이터에 접근

## OOP로 물체 모델링하기

+ 클래스: 객체가 기억해야할 것 (데이터 또는 상태)과 할 수 있는 것 (함수 또는 행동)을 정의한 코드
+ 인스턴스 (객체): 클래스로 객체를 만드는 과정
+ 메서드: 클래스 내부에서 정의된 함수
+ 객체: 데이터와 지속적으로 해당 데이터에 대해 작용하는 코드

```python
class <클래스 이름>():
   def __init__(self, <optimal param1>, ..., <optimal paramN>):
      ...
   def <함수 이름 1>(self, <optimal param1>, ..., <optimal paramN>):
      ...
   ...
   def <함수 이름 N>(self, <optimal param1>, ..., <optimal paramN>):
      ...
```

+ 스코프: 해당 변수가 접근할 수 있는 변수, 객체, 함수 집합
+ 전역 스코프: 프로그램 전역에서 접근할 수 있는 집합
+ 지역 스코프: 함수를 실행할 때만 존재가 유지되는 집합
+ 객체 스코프 (클래스 스코프, 인스턴스 스코프): 클래스 정의에 포함된 모든 코드를 구성하는 집합

+ 함수와 메서드의 차이
  + Class 선언부 다음에 반드시 들여쓰기하고 작성
  + 첫 번째 매개변수로 `self`를 가짐
  + `self.<변수명>` 방식으로 인스턴스 변수에 접근할 수 있음

## 객체의 멘털 모델과 SELF의 의미

[pythontutor.com](https://pythontutor.com/python-compiler.html#mode=edit)에서 아래와 같이 실습 진행 가능

<div align="center">
   <img width="967" alt="pythontutor.com" src="https://github.com/BOAZ-python-study/OOP-cleancode-Python/assets/42334717/2ca2a043-7603-4f87-8f90-31f879bf3c48">
</div>

<!-- 1주차 -->
<!-- 2주차 -->

## 여러 객체 관리

+ `import module` 후 `__pycache__`의 의미: 컴파일 단계를 최적화 하여 저장
+ `.pyc`: Python compiled의 약어
+ 객체 관리자 객체 (object manager object): 리스트나 딕셔너리로 객체를 관리하고 메서드를 호출하는 객체
+ 컴포지션: 한 객체가 하나 이상의 다른 객체를 관리하는 논리적인 구조
+ `Exception` 클래스를 상속하여 사용자가 지정한 예외 정의 가능

---

# 파이게임과 GUI

## 파이게임 시작하기

+ 이벤트: 프로그램이 실행 중일 때 발생하는 사건 (`pygame.event.get()`)

## 객체지향 파이게임

<p align="center">
<img width="752" alt="Screenshot 2024-02-04 at 3 30 07 AM" src="https://github.com/BOAZ-python-study/Object-Oriented-Python-Code/assets/42334717/79a1900e-af2a-4378-84dc-7309d0272219">
</p>

<!-- 2주차 -->
<!-- 3주차 -->

## 파이게임의 GUI 위젯

+ GUI 기반의 프로그램의 필수 요소
  + 윈도우 (창)
  + 포인터 기기
  + 클릭
  + 드래그
  + 소리
+ 매개변수
  + 위치 매개변수 (Positional parameter)
  + 키워드 매개변수 (Keyword parameter)

> 위치 매개변수는 키워드 매개변수보다 먼저 정의되어야 한다.

```python
def FUNCTION_NAME(POSITIONAL_PARAMETER_1, POSITIONAL_PARAMETER_2, ..., KEYWORD_PARAMETER_1=DEFAULT_VALUE_1, KEYWORD_PARAMETER_2=DEFAULT_VALUE_2, ...)
# KEYWORD_PARAMETER_1 = DEFAULT_VALUE_1와 같이 공백을 넣어 사용하지 않는 것이 관례이다.
# [1, 2, 3]과 같이 동적인 기본 값은 None으로 정의 후 조건문으로 초기화하는 것이 관례이다.
```

```bash
$ pip install pywidgets
# MACOS에서는 pywin32의 의존성 문제로 설치 불가...
```

---

# 캡슐화, 다형성, 상속

## 캡슐화

> 캡슐화 (Encapsulation): 상태 및 내부 방식의 세부 사항에 담은 모든 코드를 한 곳에 보관하고 이를 외부에서 감추는 것

+ 클라이언트 (Client): 클래스로 객체를 만들고 해당 객체의 메서드를 호출하는 모든 종류의 프로그램
+ 파이썬의 직접 접근: `{객체}.{인스턴스_변수_이름}`과 같은 방식으로 객체 변수에 접근
  + ❌ 인스턴스 변수 이름을 변경하는 상황
  + ❌ 인스턴스 변수를 계산된 값으로 만들어야하는 상황
  + ❌ 데이터 검증이 필요한 상황
+ 게터 (Getter): 클래스로 만든 객체 데이터를 조회하는 메서드
+ 세터 (Setter): 클래스로 만든 객체의 데이터 값을 할당하는 메서드
+ 인스턴스 변수의 비공개
  + 묵시적 비공개: `self._{NAME}`
  + 명시적 비공개: `self.__{NAME}`
+ 프로퍼티 (Property): 클라이언트 입장에서 보면 인스턴스 같겠지만 사실은 접근할 때 특정 메서드 대신 호출하는 클래스 속성
  + `@property`와 `@{PROPERTY_NAME}.setter` decorator를 통해 게터 및 세터 메서드 정의
  + 인스턴스 변수로의 직접 접근을 허용하지 않아 캡슐화 가능
+ 추상화 (Abstraction): 불필요한 세부 사항을 숨겨서 복잡도를 낮추는 기법

<!-- 3주차 -->
<!-- 4주차 -->

## 다형성

> 다형성 (Polymorphism): 하나가 다양한 형태를 띄는 것이 아닌 동일한 이름의 메서드를 여러 클래스가 보유하는 방법

+ 사각형, 삼각형, 원 등 도형 클래스들의 `getArea` 메서드를 개발한다면 동일한 이름의 메서드를 각 클래스에 따라 다르게 개발
+ 특수 메서드 (Special method), 매직 메서드 (Magic method)
  + `__init__`: 객체 생성 시 호출
  + `__eq__`: `==`
  + `__nq__`: `!=`
  + `__lt__`: `<`
  + `__gt__`: `>`
  + `__le__`: `<=`
  + `__ge__`: `>=`
  + `__add__`: `+`
  + `__sub__`: `-`
  + `__mul__`: `*`
  + `__truediv__`: `/`
  + `__floordiv__`: `//`
  + `__mod__`: `%`
  + `__abs__`: `abs`
  + `__str__`: `str`
  + `__repr__`: 객체 정보를 명확하고 기계가 읽을 수 있는 문자열로 변환

## 상속

> 상속 (Ingeritance): 이미 존재하는 클래스에 기초해 신규 클래스를 파생

+ 기반 클래스 (Base class), 슈퍼 클래스 (Super class), 부모 클래스 (Parent class): 상속할 클래스 (하위 클래스 기능의 기반)
+ 하위 클래스 (Subclass), 파생 클래스 (Derived class), 자식 클래스 (Child class): 상속하는 클래스 (기반 클래스 강화)
  + 기반 클래스에 정의된 메서드의 재정의 가능
  + 기반 클래스에 존재하지 않는 신규 메서드 및 인스턴스 변수 추가 가능

```python
class {SUBCLASS_NAME}({BASE_CLASS_NAME}):
    def __init__(self, ...):
        {BASE_CLASS_NAME}.__init__(self, ...)
        # super({BASE_CLASS_NAME}, self).__init__(...)
```

+ 추상 클래스 (Abstract class): 직접 객체를 생성할 의도로 작성되지 않은 클래스 (`from abc import ABC`)
+ 추상 메서드 (Abstract method): 모든 하위 클래스가 재정의해야 하는 메서드

```python
# Shape class
#
# To be used as a base class for other classes

import random
from abc import ABC, abstractmethod

# Set up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Shape(ABC):  # identifies this as an abstract base class

    def __init__(self, window, shapeType, maxWidth, maxHeight):
        self.window = window
        self.shapeType = shapeType
        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(1, maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)

    def getType(self):
        return self.shapeType

    @abstractmethod
    def clickedInside(self, mousePoint):
        raise NotImplementedError

    @abstractmethod
    def getArea(self):
        raise NotImplementedError

    @abstractmethod
    def draw(self):
        raise NotImplementedError

# Circle class

import pygame
from Shape import *
import math

class Circle(Shape):

    def __init__(self, window, maxWidth, maxHeight):
        super().__init__(window, 'Circle', maxWidth, maxHeight)
        self.radius = random.randrange(10, 50)
        self.centerX = self.x + self.radius
        self.centerY = self.y + self.radius
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        
    def clickedInside(self, mousePoint):
        theDistance = math.sqrt(((mousePoint[0] - self.centerX) ** 2) + 
                                             ((mousePoint[1] - self.centerY) ** 2))
        if theDistance <= self.radius:
            return True
        else:
            return False

    def getArea(self):
        theArea = math.pi * (self.radius ** 2)
        return theArea

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.centerX, self.centerY), self.radius, 0)
```

+ 추상 클래스 (`ABC` 상속)의 객체 생성 시 아래와 같은 에러 발생

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class Shape with abstract methods clickedInside, draw, getArea
```

<!-- 4주차 -->
<!-- 5주차 -->

## 객체가 사용하는 메모리 관리

---

# 디자인 패턴과 마무리

<!-- 5주차 -->
