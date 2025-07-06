# 객체지향 프로그래밍 가이드

## 🧾 7-1. 객체지향이란? (Object-Oriented Programming, OOP)

### 📌 객체지향이란 무엇인가요?

> 프로그램을 **'객체'라는 단위로 나누어** 만들고,
> 객체들이 **서로 메시지를 주고받으며 협력**하는 방식의 프로그래밍입니다.

### 📘 실생활 예시 1: 택배 시스템

| 구성         | 예시                                  |
| ------------ | ------------------------------------- |
| 객체(Object) | 택배 기사, 고객, 택배 물건, 배송차량  |
| 속성(변수)   | 기사: 이름, 연락처 / 물건: 무게, 크기 |
| 동작(메서드) | 배송하기, 수거하기, 위치조회          |

각 **객체는 독립적으로 존재**하고,
**자기 역할과 정보를 가지고**,
필요할 때 **다른 객체와 상호작용**합니다.

### 📘 실생활 예시 2: 커피 자판기

- 커피자판기 = 객체
- 속성: 재고, 가격, 컵 수
- 동작: 주문받기, 커피내리기, 잔액반환

```text
[버튼 누름] → [자판기: 커피 내림] → [컵 나옴]
```

### ✅ 객체지향 3대 핵심 개념

| 개념       | 뜻                             | 예시 비유                                     |
| ---------- | ------------------------------ | --------------------------------------------- |
| **캡슐화** | 속성과 기능을 하나로 묶기      | 스마트폰: 버튼만 누르면 내부 동작은 몰라도 됨 |
| **상속**   | 기존 클래스를 물려받아 재사용  | 부모 클래스 → 자식 클래스                     |
| **다형성** | 같은 기능을 다른 방식으로 구현 | `speak()` → 강아지는 "멍", 고양이는 "야옹"    |

### ✅ 절차지향 vs 객체지향 차이

| 절차지향           | 객체지향           |
| ------------------ | ------------------ |
| 명령 중심          | 객체 중심          |
| 함수 → 함수 흐름   | 객체 → 메서드 호출 |
| 코드 재사용 어려움 | 코드 재사용성 높음 |

### 🧪 미니 실습: 클래스 없는 절차지향 방식

```python
name = "홍길동"
age = 30

def introduce():
    print(f"{name}님은 {age}살입니다.")

introduce()
```

→ 상태와 동작이 **흩어져 있음**

---

## 🧾 7-2. 클래스와 객체 만들기

### 📌 클래스(class)란?

> 어떤 **객체를 만들기 위한 설계도**

- 객체: 실제로 만들어지는 개체
- 클래스: 객체를 만드는 틀(템플릿)

### ✅ 클래스 선언 기본형

```python
class 클래스이름:
    def 메서드(self):
        실행할 코드
```

- 클래스 이름은 **대문자로 시작**하는 것이 관례
- 메서드는 **함수와 비슷하지만, 반드시 `self`**를 첫 번째 인자로 가짐

### ✅ 객체(인스턴스) 생성

```python
객체이름 = 클래스이름()
```

### ✅ 예제: Dog 클래스 만들기

```python
class Dog:
    def bark(self):
        print("멍멍!")

# 객체 생성
d1 = Dog()
d1.bark()   # 출력: 멍멍!
```

## 📌 `__init__()` 메서드: 생성자

> 객체가 생성될 때 **자동으로 실행되는 함수**

```python
class Dog:
    def __init__(self, name):
        self.name = name  # 인스턴스 변수 설정

    def bark(self):
        print(f"{self.name}가 멍멍 짖습니다!")

d1 = Dog("초코")
d2 = Dog("바둑이")

d1.bark()  # 초코가 멍멍 짖습니다!
d2.bark()  # 바둑이가 멍멍 짖습니다!
```

- `__init__()`은 객체 초기 설정용
- `self.name`은 **객체마다 개별적으로 저장되는 값**

## ✅ self의 의미

- `self`는 **자기 자신(instance)**를 가리키는 변수
- 클래스 내부에서 **자신의 변수나 메서드에 접근할 때 사용**

### 🧪 실습 1: Person 클래스 만들기

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"안녕하세요! 저는 {self.name}, {self.age}살입니다.")

p1 = Person("홍길동", 25)
p2 = Person("이몽룡", 30)

p1.introduce()
p2.introduce()
```

---

## 🧾 7-3. 인스턴스 변수와 메서드

### 📌 인스턴스 변수란?

> 객체(인스턴스) **각각이 갖고 있는 고유한 정보**를 저장하는 변수입니다.

- `self.변수이름` 형식으로 사용
- 객체마다 **값이 다르게** 저장됨

### ✅ 예제: `Student` 클래스

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print(f"저는 {self.name}이고, {self.grade}학년입니다.")
```

```python
s1 = Student("홍길동", 1)
s2 = Student("이몽룡", 2)

s1.introduce()  # 저는 홍길동이고, 1학년입니다.
s2.introduce()  # 저는 이몽룡이고, 2학년입니다.
```

- `self.name`, `self.grade` → 인스턴스 변수
- `s1`과 `s2`는 **서로 다른 데이터를 가지고 있음**

## 📌 인스턴스 메서드란?

> 클래스 안에 정의된 **동작(함수)**
> 호출 시 자동으로 **자기 객체(self)**를 넘겨받음

### ✅ 메서드 내부에서 변수 변경하기

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increase(self):
        self.value += 1
        print(f"현재 값: {self.value}")
```

```python
c = Counter()
c.increase()  # 현재 값: 1
c.increase()  # 현재 값: 2
```

### ✅ 객체가 서로 독립적이라는 것 확인

```python
a = Counter()
b = Counter()

a.increase()  # a의 값만 증가
print(b.value)  # 0 (영향 없음)
```

> 각 객체는 자기만의 `value`를 가짐 (서로 격리)

## 🧪 실습 2: 은행 계좌 클래스 만들기

```python
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name}님의 잔액: {self.balance}원")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount}원 출금 완료")
        else:
            print("잔액이 부족합니다.")

# 사용 예
acc1 = BankAccount("홍길동")
acc1.deposit(10000)
acc1.withdraw(5000)
```

---

## 🧾 7-4. 클래스 변수와 인스턴스 변수의 차이

### 📌 인스턴스 변수 vs 클래스 변수

| 구분              | 정의                  | 공유 여부               | 선언 위치                       |
| ----------------- | --------------------- | ----------------------- | ------------------------------- |
| **인스턴스 변수** | 각 객체마다 따로 존재 | ❌ (개별 객체만)        | `__init__` 안에서 `self.변수명` |
| **클래스 변수**   | 모든 객체가 공유      | ✅ (전체 클래스가 공유) | 클래스 바로 아래에서 선언       |

## ✅ 예제: 고양이 클래스

```python
class Cat:
    species = "고양이"  # 클래스 변수 (모든 고양이의 공통)

    def __init__(self, name):
        self.name = name  # 인스턴스 변수 (개별 고양이의 이름)

c1 = Cat("나비")
c2 = Cat("야옹이")

print(c1.name)      # 나비
print(c2.name)      # 야옹이
print(c1.species)   # 고양이
print(c2.species)   # 고양이
```

✅ `species`는 **모든 객체가 동일하게 사용**
✅ `name`은 **각 객체마다 다름**

## ✅ 클래스 변수는 공유됨

```python
Cat.species = "고양잇과 동물"
print(c1.species)  # 고양잇과 동물
print(c2.species)  # 고양잇과 동물
```

> **클래스 변수 하나만 바꿔도 전체 인스턴스에 반영**

## ✅ 인스턴스에서 클래스 변수 수정?

```python
c1.species = "개"
print(c1.species)  # 개 (인스턴스에 새로 생성된 변수!)
print(c2.species)  # 고양잇과 동물
```

> 클래스 변수와 **같은 이름의 인스턴스 변수를 새로 만든 것**일 뿐
> 클래스 변수는 그대로입니다.

## 🧪 실습 3: 인스턴스 수 세기

```python
class Counter:
    count = 0  # 클래스 변수

    def __init__(self):
        Counter.count += 1
        print(f"{Counter.count}번째 인스턴스 생성됨")

a = Counter()
b = Counter()
c = Counter()
```

> 클래스 전체에서 공유되는 `count` 변수를 사용해 **생성된 인스턴스 개수 추적**

---

## 🧾 7-5. 클래스의 상속 (Inheritance)

### 📌 상속이란?

> 기존 클래스를 **물려받아**, 새로운 클래스를 **확장하거나 변경**할 수 있는 기능

- 기존 클래스: **부모 클래스(Parent / Superclass)**
- 새 클래스: **자식 클래스(Child / Subclass)**

### ✅ 상속의 기본 문법

```python
class 부모클래스:
    ...

class 자식클래스(부모클래스):
    ...
```

> 자식 클래스는 부모 클래스의 **속성과 메서드를 그대로 사용할 수 있음**

### ✅ 예제: `Person` → `Student` 상속

```python
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"안녕하세요, {self.name}입니다.")

class Student(Person):
    def study(self):
        print(f"{self.name}는 공부 중입니다.")
```

```python
s = Student("홍길동")
s.introduce()  # 부모 메서드
s.study()      # 자식 메서드
```

✅ `Student`는 `Person`의 기능을 그대로 **상속받아 사용 가능**

- 본인만의 기능도 추가할 수 있음

## ✅ 생성자 오버라이드와 `super()`

자식 클래스에서 `__init__()`을 **재정의하면**, 부모의 초기화는 안 불림
→ **`super()`로 부모 생성자를 호출해야 함**

```python
class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)     # 부모 생성자 호출
        self.grade = grade

    def study(self):
        print(f"{self.name}는 {self.grade}학년이고 공부 중입니다.")
```

```python
s = Student("이몽룡", 2)
s.introduce()
s.study()
```

### ✅ `super()`란?

> 부모 클래스의 메서드나 생성자를 **가져와 실행**할 수 있게 해주는 내장 함수

## 🧪 실습 4: Animal → Dog 상속 구조 만들기

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("동물이 소리 낸다")

class Dog(Animal):
    def bark(self):
        print(f"{self.name}가 멍멍!")

d = Dog("초코")
d.speak()  # 부모 메서드
d.bark()   # 자식 메서드
```

---

## 🧾 7-6. 메서드 오버라이딩 (Overriding)

### 📌 오버라이딩이란?

> 부모 클래스에서 정의된 메서드를
> **자식 클래스에서 같은 이름으로 다시 정의하는 것**

→ 기존 기능을 **그 상황에 맞게 바꿔서 사용**할 수 있음

### ✅ 기본 예제

```python
class Animal:
    def sound(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):
    def sound(self):
        print("멍멍!")

class Cat(Animal):
    def sound(self):
        print("야옹~")
```

```python
a = Animal()
d = Dog()
c = Cat()

a.sound()  # 동물이 소리를 냅니다.
d.sound()  # 멍멍!
c.sound()  # 야옹~
```

- 같은 `sound()` 메서드지만 클래스에 따라 동작이 달라짐
- 이것이 **다형성(polymorphism)**의 핵심 예시이기도 함

## ✅ 오버라이딩 + super() 함께 쓰기

```python
class Animal:
    def sound(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):
    def sound(self):
        super().sound()  # 부모의 sound도 호출
        print("멍멍!")

d = Dog()
d.sound()
```

출력:
```
동물이 소리를 냅니다.
멍멍!
```

- 자식 클래스에서 **부모 기능을 유지하면서 추가**하고 싶을 때 사용

## 🧪 실습 5: 소개 메서드 오버라이딩

```python
class Person:
    def introduce(self):
        print("안녕하세요. 사람입니다.")

class Student(Person):
    def introduce(self):
        print("안녕하세요. 학생입니다.")

p = Person()
s = Student()

p.introduce()  # 안녕하세요. 사람입니다.
s.introduce()  # 안녕하세요. 학생입니다.
```

---

## 🧾 7-7. 캡슐화와 접근제어

### 📌 캡슐화(Encapsulation)란?

> 객체의 **속성(변수)**을 외부에서 **직접 접근하지 못하게 보호**하고,
> 대신 **메서드를 통해 간접적으로 접근하도록 만드는 것**

### ✅ 왜 캡슐화가 필요한가요?

| 이유           | 설명                                             |
| -------------- | ------------------------------------------------ |
| 내부 상태 보호 | 실수로 변수 값을 잘못 바꾸는 것을 방지           |
| 안정성 확보    | 잘못된 값이 들어가지 않도록 검증 가능            |
| 유지보수 쉬움  | 인터페이스를 유지하면서 내부 구현만 바꿀 수 있음 |

## ✅ 접근 제어자 (비공식 규칙)

| 방식      | 사용 예시   | 의미                                     |
| --------- | ----------- | ---------------------------------------- |
| public    | `self.name` | 어디서든 접근 가능                       |
| protected | `_name`     | 내부용 (접근은 가능하지만 권장하지 않음) |
| private   | `__name`    | 외부에서 접근 불가 (이름 맹글링 처리됨)  |

### ✅ 예제: 비공개 변수와 getter/setter

```python
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # 외부에서 접근 불가

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("❌ 금액은 음수가 될 수 없습니다.")

acc = Account("홍길동", 10000)

print(acc.name)               # 홍길동
# print(acc.__balance)       # ❌ 접근 불가 (에러 발생)
print(acc.get_balance())      # ✅ 10000

acc.set_balance(20000)        # ✅ 금액 변경
acc.set_balance(-500)         # ❌ 음수 방지
```

### ✅ `__변수명`의 비밀

```python
print(acc.__balance)         # ❌ AttributeError

print(acc._Account__balance) # 가능하지만 ❌ 권장하지 않음
```

> `__변수명` → 내부적으로 `_클래스명__변수명`으로 변경되어 저장됨
> → 진짜 private은 아니지만, **실수 방지를 위한 장치**

## 🧪 실습 6: 보호된 속성을 갖는 자동차 클래스

```python
class Car:
    def __init__(self, brand):
        self._speed = 0
        self.brand = brand

    def accelerate(self, amount):
        self._speed += amount
        print(f"{self.brand} 속도: {self._speed}km/h")

c = Car("현대")
c.accelerate(30)
print(c._speed)  # 가능은 하지만 직접 접근은 권장되지 않음
```

---

## 🧾 7-8. 실습: 부동산 매물 클래스 만들기

### 🎯 목표

- 부동산 매물 객체를 만들고 여러 매물 정보를 관리해보기
- 실제로 많이 쓰이는 부동산 정보를 모델링

### ✅ 클래스 설계

```python
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(f"{self.location} {self.house_type} ({self.completion_year}년 준공)")
        print(f"[거래: {self.deal_type}] 가격: {self.price}")
```

### ✅ 객체 생성 및 리스트에 저장

```python
house1 = House("강남", "아파트", "매매", "15억", 2003)
house2 = House("마포", "오피스텔", "전세", "5억", 2010)
house3 = House("송파", "빌라", "월세", "500/50", 1995)

houses = [house1, house2, house3]
```

### ✅ 출력 기능 구현

```python
print(f"총 {len(houses)}개의 매물이 있습니다.\n")

for house in houses:
    house.show_detail()
    print("-" * 30)
```

### 💡 출력 예시

```
총 3개의 매물이 있습니다.

강남 아파트 (2003년 준공)
[거래: 매매] 가격: 15억
------------------------------
마포 오피스텔 (2010년 준공)
[거래: 전세] 가격: 5억
------------------------------
...
```

---

## 🧾 7-9. 실습: 학생 출석부 클래스 만들기

### 🎯 목표

- 학생마다 이름, 학번, 출석 상태를 저장하는 클래스를 설계
- 여러 학생을 리스트로 관리
- 출석 처리 / 조회 기능 구현

### ✅ 클래스 설계

```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.attendance = False  # 기본값: 결석(False)

    def check_attendance(self):
        self.attendance = True

    def show_status(self):
        status = "출석" if self.attendance else "결석"
        print(f"{self.student_id} {self.name}: {status}")
```

### ✅ 객체 생성 및 리스트 관리

```python
students = [
    Student("홍길동", "202301"),
    Student("성춘향", "202302"),
    Student("이몽룡", "202303"),
]
```

### ✅ 출석 처리하기

```python
students[0].check_attendance()
students[2].check_attendance()
```

### ✅ 전체 출석 현황 출력

```python
print("📋 오늘의 출석 현황")

for s in students:
    s.show_status()
```

### 💡 출력 예시

```
📋 오늘의 출석 현황
202301 홍길동: 출석
202302 성춘향: 결석
202303 이몽룡: 출석
```

### 🧪 도전 과제: 사용자 입력 기반 출석 체크

```python
for student in students:
    answer = input(f"{student.name} 출석했나요? (y/n): ")
    if answer.lower() == "y":
        student.check_attendance()
```

---

## ✅ 7장 마무리 요약

| 개념          | 핵심 내용                       |
| ------------- | ------------------------------- |
| 클래스        | 객체를 만들기 위한 설계도       |
| 인스턴스      | 실제로 만들어진 객체            |
| `__init__`    | 생성자, 초기값 설정             |
| `self`        | 자기 자신 객체                  |
| 인스턴스 변수 | 객체마다 다른 데이터            |
| 클래스 변수   | 객체끼리 공유하는 데이터        |
| 상속          | 부모의 속성과 기능을 물려받음   |
| 오버라이딩    | 부모 기능을 자식이 재정의       |
| 캡슐화        | 내부 상태 보호 (비공개 변수 등) |