# 5장. 함수(Function)

## 🧭 전체 개요

### ✅ 학습 목표
- **코드의 재사용성과 구조화**를 위한 함수 개념을 이해한다.
- **인자(입력)**, **반환값(출력)**, **기본값**, **가변 인자**, **변수의 범위** 등 함수를 다룰 수 있는 필수 능력을 기른다.
- 나만의 함수를 만들고, 호출하고, 활용할 수 있다.

### 📚 전체 구성

| 섹션 | 제목 | 주요 내용 |
|------|------|-----------|
| 5-1 | 함수란 무엇인가? | 함수의 정의, 필요성, 구조 |
| 5-2 | 함수 정의와 호출 | `def`, `return`, 호출 방법 |
| 5-3 | 인자와 매개변수 | 위치 인자, 기본값, 키워드 인자 |
| 5-4 | 가변 인자와 키워드 인자 | `*args`, `**kwargs` 사용법 |
| 5-5 | 반환값 다루기 | 여러 값 반환, return의 위치 |
| 5-6 | 변수의 범위 | 지역변수 vs 전역변수 |
| 5-7 | lambda 함수 | 한 줄 함수, 표현식 함수 |
| 5-8 | 실습: BMI 계산기 함수 | 입력 → 계산 → 메시지 출력 |
| 5-9 | 실습: 은행 계좌 시뮬레이터 | 입금, 출금, 이체 등 함수로 분리 |

---

## 5-1. 함수란 무엇인가?

### 📌 함수(Function)란?
> 어떤 **기능을 하나로 묶은 코드 블록**으로, **필요할 때마다 호출해서 재사용**할 수 있습니다.

### ✅ 함수의 장점
- **코드의 재사용성 향상**
- **가독성** 높아짐
- 유지보수 용이
- 복잡한 프로그램을 **작은 단위로 나누어 구조화** 가능

### ✅ 함수 사용 전/후 비교

#### 💨 사용 전 (중복 코드)
```python
print("안녕하세요!")
print("저는 홍길동입니다.")
print("반갑습니다.")
```

#### 💡 함수 사용 후
```python
def introduce():
    print("안녕하세요!")
    print("저는 홍길동입니다.")
    print("반갑습니다.")

introduce()
```

### 🧪 실습 1: 나만의 인사 함수 만들기
```python
def say_hello():
    print("Hello, Python!")

say_hello()
say_hello()
```

---

## 5-2. 함수 정의와 호출

### 📌 함수 정의하기
> `def` 키워드를 사용하여 함수를 정의합니다.

```python
def 함수이름():
    실행할 코드
```

예:
```python
def say_hello():
    print("안녕하세요!")
```

### 📌 함수 호출하기
정의한 함수를 호출하면 해당 코드 블록이 실행됩니다.

```python
say_hello()  # 함수 실행
```

### 📌 `return` 문 – 결과를 반환하는 키워드
함수가 **계산 결과나 값**을 돌려줄 때 사용합니다.

```python
def get_name():
    return "홍길동"

name = get_name()
print(name)  # 홍길동
```

> `return`을 만나면 함수는 그 즉시 종료되고 값을 돌려줍니다.

### 📌 `None`의 개념
`return`이 없는 함수는 **자동으로 `None`을 반환**합니다.

```python
def no_return():
    print("출력만 하고 끝")

result = no_return()
print(result)  # None
```

### 🧪 실습 2: 두 수의 합을 반환하는 함수 만들기
```python
def add(a, b):
    return a + b

result = add(10, 5)
print("결과:", result)
```

### 🧪 실습 3: 환영 메시지 반환 함수 만들기
```python
def welcome(name):
    return f"{name}님, 환영합니다!"

msg = welcome("이몽룡")
print(msg)
```

---

## 5-3. 함수의 인자와 매개변수

### 📌 개념 구분

| 용어 | 설명 |
|------|------|
| 매개변수(Parameter) | 함수 정의 시 받는 입력값 이름 |
| 인자(Argument) | 함수 호출 시 실제로 넘기는 값 |

```python
def greet(name):     # name: 매개변수
    print(f"안녕하세요, {name}님!")

greet("성춘향")        # "성춘향": 인자
```

### 📌 위치 인자 (Positional Argument)
인자의 **순서대로 매개변수에 대응**됩니다.

```python
def introduce(name, age):
    print(f"{name}은 {age}살입니다.")

introduce("홍길동", 20)
```

### 📌 기본값 인자 (Default Argument)
매개변수에 **기본값을 지정**할 수 있습니다.

```python
def greet(name, message="반가워요"):
    print(f"{name}님, {message}!")

greet("이몽룡")            # 기본값 사용
greet("임꺽정", "오랜만이네요")  # 사용자 값 사용
```

### 📌 키워드 인자 (Keyword Argument)
함수 호출 시 인자의 이름을 직접 지정할 수 있습니다.

```python
def order(menu, size):
    print(f"{size} 사이즈의 {menu} 주문 완료!")

order(size="Large", menu="아메리카노")
```

### 🧪 실습 4: 자기소개 함수 만들기
```python
def introduce(name, job="학생"):
    print(f"안녕하세요, 저는 {name}이고 {job}입니다.")

introduce("박문수")                      # 기본 직업 사용
introduce("홍길동", job="개발자")         # 키워드 인자 사용
```

---

## 5-4. 가변 인자와 키워드 인자

### 📌 `*args` : 여러 개의 **위치 인자** 받기
> 함수가 받을 **인자의 개수가 정해지지 않았을 때** 사용합니다.

```python
def print_scores(*args):
    for score in args:
        print("점수:", score)

print_scores(80, 90, 75)
```

- `args`는 **튜플 형태**로 전달됩니다.

### 📌 `**kwargs` : 여러 개의 **키워드 인자** 받기
> 인자들이 `key=value` 형태로 전달될 때 사용합니다.

```python
def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_profile(name="이몽룡", age=20, job="학생")
```

- `kwargs`는 **딕셔너리 형태**로 전달됩니다.

### 📌 함께 사용할 때 주의사항
순서는 다음과 같이 써야 합니다:

```python
def func(a, b=0, *args, **kwargs):
    ...
```

> 위치 인자 → 기본값 인자 → `*args` → `**kwargs`

### 🧪 실습 5: 쇼핑 목록 함수 만들기 (`*args`)
```python
def show_cart(*items):
    print("장바구니 목록:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

show_cart("우유", "계란", "식빵", "딸기")
```

### 🧪 실습 6: 회원 정보 등록 함수 (`**kwargs`)
```python
def register(**info):
    print("회원 정보:")
    for k, v in info.items():
        print(f"{k} → {v}")

register(name="홍길동", age=30, phone="010-1234-5678")
```

---

## 5-5. 반환값 다루기

### 📌 기본적인 `return`
```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8
```

### 📌 여러 값을 반환하기 (튜플 형태)
```python
def calc(a, b):
    return a + b, a - b

sum_result, diff_result = calc(10, 4)
print("합:", sum_result)
print("차:", diff_result)
```

### 📌 조건에 따라 다른 값 반환하기
```python
def check_even(n):
    if n % 2 == 0:
        return "짝수"
    else:
        return "홀수"
```

### 📌 반환 없이 종료만 하기 (`return` 단독 사용)
```python
def greet(name):
    if not name:
        return
    print(f"{name}님, 안녕하세요!")

greet("")   # 출력 없음
greet("홍길동")  # 출력됨
```

### 🧪 실습 7: 사칙연산 함수 만들기
```python
def calculate(a, b):
    return a + b, a - b, a * b, a / b

add, sub, mul, div = calculate(8, 2)
print("덧셈:", add)
print("나눗셈:", div)
```

### 🧪 실습 8: 학생 합격 여부 판별기
```python
def is_pass(score):
    if score >= 60:
        return "합격"
    return "불합격"

print(is_pass(75))  # 합격
print(is_pass(45))  # 불합격
```

---

## 5-6. 변수의 범위 (Scope)

### 📌 지역변수 (Local Variable)
> 함수 **안에서 선언된 변수**는 **그 함수 안에서만 유효**합니다.

```python
def greet():
    message = "Hello"
    print(message)

greet()
# print(message)  # 에러! message는 함수 바깥에서 쓸 수 없음
```

### 📌 전역변수 (Global Variable)
> 함수 **밖에서 선언된 변수**는 프로그램 전체에서 사용 가능

```python
name = "홍길동"

def say_name():
    print("이름:", name)

say_name()  # "이름: 홍길동"
```

### 📌 전역변수 수정하기 – `global` 키워드
> 함수 안에서 전역변수를 **읽을 수는 있지만**, **수정하려면 반드시 `global` 선언**이 필요합니다.

```python
count = 0

def increase():
    global count
    count += 1

increase()
print(count)  # 1
```

### 📌 주의: 지역변수가 전역변수를 가리기(SHADOWING)
```python
x = 10

def func():
    x = 5  # 지역변수 x → 전역 x를 가림
    print("x in function:", x)

func()
print("x outside:", x)
```

출력:
```
x in function: 5
x outside: 10
```

### 🧪 실습 9: 지역변수와 전역변수 구분 실험
```python
msg = "Hello"

def change_msg():
    msg = "Hi"
    print("함수 안:", msg)

change_msg()
print("함수 밖:", msg)
```

### 🧪 실습 10: 전역 변수 누적기 (`global` 사용)
```python
total = 0

def add_to_total(n):
    global total
    total += n

add_to_total(5)
add_to_total(10)
print("총합:", total)  # 15
```

---

## 5-7. `lambda` 함수 (익명 함수)

### 📌 `lambda` 함수란?
> 이름 없이 한 줄로 작성하는 **간단한 함수 표현식**

```python
lambda 매개변수: 표현식
```

### ✅ 일반 함수 vs `lambda` 함수 비교
```python
# 일반 함수
def add(x, y):
    return x + y

# lambda 함수
add_lambda = lambda x, y: x + y

print(add(3, 5))         # 8
print(add_lambda(3, 5))  # 8
```

### 📌 언제 사용하나요?
- **간단한 함수**를 **일시적으로 사용**할 때
- **정렬, 필터링, map 등 함수형 프로그래밍**에서 자주 사용

### 📌 예제: 리스트 정렬 기준으로 lambda 사용
```python
students = [
    ("홍길동", 85),
    ("이몽룡", 90),
    ("성춘향", 70)
]

# 점수 기준으로 정렬
students.sort(key=lambda x: x[1])
print(students)
```

### 🧪 실습 11: 짝수인지 판별하는 lambda 함수
```python
is_even = lambda x: x % 2 == 0
print(is_even(4))  # True
print(is_even(5))  # False
```

### 🧪 실습 12: 문자열 길이로 정렬
```python
words = ["apple", "hi", "banana", "go"]

words.sort(key=lambda x: len(x))
print(words)  # ['hi', 'go', 'apple', 'banana']
```

---

## 5-8. 실습 예제: BMI 계산기 함수

### 🎯 목표
- 입력값(키, 몸무게)을 받아
- **BMI 계산 → 결과에 따른 메시지 반환**
- 함수로 설계하고 호출하는 패턴 익히기

### 📌 BMI 공식
> BMI = 체중(kg) / (신장(m)²)

### ✅ 함수 설계
```python
def calc_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def interpret_bmi(bmi):
    if bmi >= 25:
        return "과체중입니다."
    elif bmi >= 18.5:
        return "정상 체중입니다."
    else:
        return "저체중입니다."

def run_bmi():
    height = float(input("키(cm): "))
    weight = float(input("몸무게(kg): "))
    bmi = calc_bmi(weight, height)
    print(f"BMI: {bmi}")
    print(interpret_bmi(bmi))

run_bmi()
```

---

## 5-9. 실습 예제: 은행 계좌 시뮬레이터

### 🎯 기능 요구사항
- 입금하기
- 출금하기
- 잔액 조회
- 프로그램 종료

### ✅ 전체 코드
```python
balance = 0  # 전역 변수: 현재 잔액

def deposit(amount):
    global balance
    balance += amount
    print(f"{amount}원이 입금되었습니다. 현재 잔액: {balance}원")

def withdraw(amount):
    global balance
    if amount > balance:
        print("잔액이 부족합니다.")
    else:
        balance -= amount
        print(f"{amount}원이 출금되었습니다. 현재 잔액: {balance}원")

def check_balance():
    print(f"현재 잔액은 {balance}원입니다.")

def run_bank():
    while True:
        print("\n📋 은행 메뉴")
        print("1. 입금")
        print("2. 출금")
        print("3. 잔액 조회")
        print("4. 종료")
        choice = input("번호를 선택하세요: ")

        if choice == "1":
            amt = int(input("입금할 금액: "))
            deposit(amt)
        elif choice == "2":
            amt = int(input("출금할 금액: "))
            withdraw(amt)
        elif choice == "3":
            check_balance()
        elif choice == "4":
            print("이용해주셔서 감사합니다.")
            break
        else:
            print("잘못된 선택입니다.")

run_bank()
```

---

## 🎉 함수 개념 요약

| 개념 | 설명 |
|------|------|
| `def` | 함수 정의 |
| `return` | 함수 결과 반환 |
| 매개변수/인자 | 함수 입력값 전달 방식 |
| 기본값/키워드 인자 | 유연한 호출 방식 |
| `*args`, `**kwargs` | 가변 인자 처리 |
| 지역/전역변수 | 변수 범위 구분 |
| `lambda` | 간단한 익명 함수 |