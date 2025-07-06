| 단원 | 제목                | 주요 내용                             | 관련 모듈          |
| ---- | ------------------- | ------------------------------------- | ------------------ |
| 6-1  | 파일 입출력이란?    | 개념, 흐름, 왜 필요한가               | 없음               |
| 6-2  | 파일 열기와 닫기    | `open()`, 모드, 인코딩                | `open()`           |
| 6-3  | 파일 쓰기           | `write()`, 줄바꿈 처리                | `open()`           |
| 6-4  | 파일 읽기           | `read()`, `readline()`, `readlines()` | `open()`           |
| 6-5  | `with` 문 활용      | 안전하게 파일 열고 닫기               | `with`             |
| 6-6  | 폴더 다루기         | 폴더 생성, 확인, 경로 조작            | `os`, `pathlib`    |
| 6-7  | 파일 다루기         | 존재 확인, 삭제, 변경                 | `os`, `pathlib`    |
| 6-8  | 파일 복사/이동/삭제 | 복사, 이동, 압축                      | `shutil`           |
| 6-9  | CSV 파일 읽고 쓰기  | `csv.reader()`, `csv.writer()`        | `csv`              |
| 6-10 | 실습: 일기 쓰기     | 날짜 포함 txt 저장                    | `datetime`, `with` |
| 6-11 | 실습: 출석부 분석기 | CSV → 리스트/딕셔너리                 | `csv`, `os`        |

---

## 🧾 6-1. 파일 입출력이란?

### 📌 파일 입출력이란?

> 파이썬 프로그램에서 **텍스트 파일과 데이터를 읽고 쓰는 것**

### ✅ Input / Output 개념 정리

| 구분   | 뜻   | 예시                         |
| ------ | ---- | ---------------------------- |
| Input  | 입력 | 파일에서 정보를 **가져오기** |
| Output | 출력 | 정보를 파일에 **저장하기**   |

### 📘 실생활 비유

> **컴퓨터 = 주방, 파일 = 냉장고**, 프로그램 = 요리사

- `입력(input)` = 냉장고에서 재료 꺼내오기
- `출력(output)` = 완성된 요리를 다시 냉장고에 넣기

> 즉, 파일 입출력은 프로그램이 **외부 저장 공간과 정보를 주고받는 일**입니다.

### ✅ 왜 배워야 하나요?

| 이유                           | 설명                             |
| ------------------------------ | -------------------------------- |
| 프로그램 종료 시 값이 사라짐   | 메모리는 휘발성, 파일은 저장성   |
| 사용자 입력 결과 저장          | 예: 일기장, 계산 기록, 성적표    |
| 저장된 데이터로 다시 실행 가능 | 예: 출석부 불러오기, 게임 세이브 |

### ✅ 입출력 기본 흐름도

```
1. open("파일경로", "모드") → 파일 열기
2. write()/read() → 내용 쓰기/읽기
3. close() → 파일 닫기
```

### 예시 미리보기

```python
f = open("hello.txt", "w")
f.write("Hello, file!")
f.close()
```

- `"w"`: 쓰기 모드
- `f.write(...)`: 내용 쓰기
- `f.close()`: 저장 후 닫기

---

## 🧾 6-2. 파일 열기와 닫기 (`open()`, `close()`)

### 📌 `open()` 함수란?

> 파이썬에서 **파일을 다루려면 가장 먼저 `open()`으로 열어야 합니다.**

```python
파일객체 = open("파일경로", "모드")
```

- `"파일경로"` : 열고 싶은 파일의 이름이나 경로
- `"모드"` : 어떻게 열 건지 (쓰기, 읽기, 추가 등)

### ✅ 대표적인 파일 모드 (mode)

| 모드  | 의미                             | 사용 예시                   |
| ----- | -------------------------------- | --------------------------- |
| `"r"` | 읽기 모드 (기본값)               | 파일 내용 읽기              |
| `"w"` | 쓰기 모드                        | 기존 내용 삭제 후 새로 쓰기 |
| `"a"` | 추가 모드                        | 기존 내용 뒤에 덧붙이기     |
| `"x"` | 새 파일 쓰기 (파일 존재 시 에러) | 안전한 새 파일 생성         |
| `"b"` | 바이너리 모드                    | 이미지, 동영상 등           |

> 일반 텍스트 파일은 `"r"`, `"w"`, `"a"`를 주로 사용합니다.

### ✅ 파일 열기 + 쓰기 예제

```python
f = open("test.txt", "w")  # 쓰기 모드로 열기
f.write("파일에 글을 씁니다.")
f.close()
```

> 🔐 **꼭 `close()`로 닫아야 파일이 저장되고 잠금 해제됩니다.**

### ✅ 파일 열기 + 읽기 예제

```python
f = open("test.txt", "r")
text = f.read()
print("파일 내용:", text)
f.close()
```

### ❗ 자주 하는 실수

```python
f = open("없는파일.txt", "r")  # ❌ 에러 발생
```

> `r` 모드는 파일이 없으면 **FileNotFoundError** 발생
> → 해결: `"w"` 또는 `"x"`로 생성하거나 `os.path.exists()`로 먼저 확인

### 🧪 실습 1: 텍스트 파일 생성하고 저장

```python
f = open("my_note.txt", "w")
f.write("오늘은 파이썬 수업을 들었습니다.\n재밌었어요!")
f.close()
```

### 🧪 실습 2: 파일 내용 읽기

```python
f = open("my_note.txt", "r")
text = f.read()
print("저장된 글:\n", text)
f.close()
```

---

## 🧾 6-3. 파일 쓰기: `write()` 함수

### 📌 `write()` 함수란?

> **파일에 문자열 데이터를 쓰는 함수**

```python
f = open("example.txt", "w")
f.write("안녕하세요!")     # 한 줄 쓰기
f.close()
```

- `"w"` 모드: 기존 내용이 있으면 **모두 지우고 새로 씀**
- `write()`는 **자동 줄바꿈이 없음**

### ✅ 줄바꿈하려면 `\n`을 직접 넣기

```python
f = open("multi_line.txt", "w")
f.write("첫 번째 줄\n")
f.write("두 번째 줄\n")
f.write("세 번째 줄\n")
f.close()
```

### 📌 리스트를 한 번에 파일에 쓰기 (`writelines()`)

```python
lines = ["사과\n", "바나나\n", "딸기\n"]
f = open("fruits.txt", "w")
f.writelines(lines)
f.close()
```

- `writelines()`는 리스트의 각 요소를 파일에 **연속적으로 씀**
- 요소마다 `\n`이 포함되어 있어야 줄바꿈됨

### ✅ `write()` vs `writelines()` 비교

| 함수                   | 특징                                   |
| ---------------------- | -------------------------------------- |
| `write("문자열")`      | 한 줄씩 직접 작성                      |
| `writelines([리스트])` | 여러 줄 한꺼번에 쓰기 (줄바꿈 \n 필수) |

### 🧪 실습 3: 오늘의 할 일 저장하기

```python
f = open("todo.txt", "w")
f.write("1. 파이썬 수업 듣기\n")
f.write("2. 점심 먹기\n")
f.write("3. 복습하기\n")
f.close()
```

### 🧪 실습 4: 리스트를 파일로 쓰기

```python
todos = ["공부하기\n", "산책하기\n", "책 읽기\n"]
f = open("list.txt", "w")
f.writelines(todos)
f.close()
```

---

## 🧾 6-4. 파일 읽기: `read()`, `readline()`, `readlines()`

### ✅ 먼저 파일 준비

이 예제에서는 미리 아래와 같은 텍스트 파일이 있다고 가정합니다 (`memo.txt`):

```
첫 번째 줄입니다.
두 번째 줄입니다.
세 번째 줄입니다.
```

## ① `read()` – 전체 내용 한꺼번에 읽기

```python
f = open("memo.txt", "r")
content = f.read()
print(content)
f.close()
```

- 파일 전체를 **하나의 문자열로** 읽어옴
- 소규모 텍스트 파일에 적합
- 줄바꿈 문자(`\n`) 포함됨

## ② `readline()` – 한 줄씩 읽기 (한 줄만!)

```python
f = open("memo.txt", "r")
line1 = f.readline()
line2 = f.readline()
print("1:", line1.strip())
print("2:", line2.strip())
f.close()
```

- 호출할 때마다 한 줄씩 읽음
- `strip()`은 줄 끝의 `\n` 제거
- 큰 파일을 줄 단위로 처리할 때 유용

## ③ `readlines()` – 전체 줄을 리스트로 읽기

```python
f = open("memo.txt", "r")
lines = f.readlines()
f.close()

for i, line in enumerate(lines, 1):
    print(f"{i}번째 줄: {line.strip()}")
```

- 각 줄이 리스트의 원소가 됨
- 한꺼번에 메모리에 올려야 하므로 **중간 크기 이하의 파일에 적합**

### ✅ 세 가지 방식 비교

| 함수          | 설명             | 결과 타입 |
| ------------- | ---------------- | --------- |
| `read()`      | 전체 읽기        | 문자열    |
| `readline()`  | 한 줄씩 읽기     | 문자열    |
| `readlines()` | 전체 줄 리스트로 | 리스트    |

### 🧪 실습 5: 좋아하는 음식 리스트 출력하기

```python
f = open("food.txt", "r")
foods = f.readlines()
f.close()

print("내가 좋아하는 음식:")
for food in foods:
    print("-", food.strip())
```

---

## 🧾 6-5. `with` 문으로 안전하게 파일 다루기

### 📌 `with` 문이란?

> 파일을 사용할 때 **자동으로 닫아주는 안전한 방법**

```python
with open("파일이름", "모드") as 파일변수:
    파일작업...
```

- `파일변수`는 파일 객체 (`f`, `file`, 등)
- 블록이 끝나면 `close()`가 **자동으로 실행**

### ✅ 기존 방식 (`open` + `close`)

```python
f = open("hello.txt", "w")
f.write("안녕하세요")
f.close()  # ❗ 안 쓰면 파일이 닫히지 않음
```

> 실수로 `close()`를 빼먹으면 **파일이 저장되지 않거나, 다른 프로그램에서 잠김 현상 발생**

### ✅ `with` 문 방식 (권장 ✅)

```python
with open("hello.txt", "w") as f:
    f.write("안녕하세요")  # 자동 저장 + 닫힘
```

- 코드가 짧고 안정적
- 예외가 발생해도 파일은 자동으로 닫힘

### ✅ 읽기 예제

```python
with open("hello.txt", "r") as f:
    content = f.read()
    print(content)
```

### 🧪 실습 6: 일기 저장하기

```python
diary = input("오늘 하루를 한 줄로 정리해보세요: ")

with open("diary.txt", "a", encoding="utf-8") as f:
    f.write(diary + "\n")

print("일기가 저장되었습니다.")
```

- `"a"` : 기존 내용에 **추가 쓰기**
- `encoding="utf-8"` : 한글 깨짐 방지

### ✅ 파일 인코딩이란?

> 글자가 어떻게 저장되는지를 정하는 약속

| 인코딩    | 설명                                       |
| --------- | ------------------------------------------ |
| `"utf-8"` | 전 세계 공통, 한글 지원, 기본값            |
| `"cp949"` | 윈도우 기본 한글 인코딩 (엑셀 등에서 사용) |

```python
with open("file.txt", "r", encoding="utf-8") as f:
    ...
```

---

## 🧾 6-6. 폴더 다루기 (`os`, `pathlib`)

### 📌 폴더(디렉토리)를 왜 다뤄야 하나요?

- 프로그램이 만든 **파일을 자동으로 정리**할 수 있음
- 예: `logs/`, `output/`, `backup/` 폴더 만들기
- 플랫폼에 상관없이 **폴더 경로를 정확히 처리**해야 함

## ✅ 방법 ①: `os` 모듈 사용

### 📌 폴더 존재 확인 및 생성

```python
import os

folder_name = "output"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("폴더 생성 완료!")
else:
    print("이미 폴더가 있습니다.")
```

- `os.path.exists(path)` → 폴더나 파일이 있는지 확인
- `os.mkdir(path)` → 폴더 생성 (1단계만 가능)

### 📌 하위 폴더까지 생성: `os.makedirs()`

```python
os.makedirs("output/data/2025", exist_ok=True)
```

- `exist_ok=True`: 이미 있으면 에러 없이 넘어감

## ✅ 방법 ②: `pathlib.Path` 객체 사용 (추천 🌟)

```python
from pathlib import Path

p = Path("output")
if not p.exists():
    p.mkdir()
    print("폴더 생성 완료!")
```

- `Path()` → 경로 객체
- `mkdir()` → 폴더 생성
- 가독성이 높고, 윈도우/리눅스 경로 구분도 자동 처리

### ✅ 하위 폴더까지 만들기

```python
Path("output/data/2025").mkdir(parents=True, exist_ok=True)
```

### ✅ 경로 합치기 (플랫폼 호환 방식)

```python
folder = Path("output")
file = folder / "result.txt"   # 경로 자동 연결
```

> `"output/result.txt"` 처럼 슬래시(`/`) 직접 쓰지 않아도 됨
> 윈도우와 리눅스에서도 **자동 호환**

### 🧪 실습 7: 결과 저장용 폴더 만들기

```python
from pathlib import Path

output_path = Path("result")
output_path.mkdir(exist_ok=True)

with open(output_path / "summary.txt", "w", encoding="utf-8") as f:
    f.write("실험 결과 저장 완료")
```

---

## 🧾 6-7. 파일 다루기 (`os`, `pathlib`)

## ✅ 1. 파일 존재 여부 확인

### 📌 방법 ①: `os.path.exists()`

```python
import os

if os.path.exists("test.txt"):
    print("파일이 존재합니다.")
else:
    print("파일이 없습니다.")
```

### 📌 방법 ②: `Path.exists()`

```python
from pathlib import Path

p = Path("test.txt")
if p.exists():
    print("파일 있음")
```

## ✅ 2. 파일 삭제

### 📌 `os.remove()` – 파일 삭제

```python
import os

if os.path.exists("old.txt"):
    os.remove("old.txt")
    print("삭제 완료")
```

> ❗ 존재하지 않으면 `FileNotFoundError`

### 📌 `Path.unlink()` – 삭제 (pathlib 방식)

```python
from pathlib import Path

f = Path("old.txt")
if f.exists():
    f.unlink()
    print("삭제 완료")
```

## ✅ 3. 파일 이름 바꾸기 (= 이동)

### 📌 `os.rename(원래이름, 새이름)`

```python
import os

os.rename("result.txt", "result_backup.txt")
```

- 이름 바꾸기뿐 아니라 **다른 폴더로 이동도 가능**

```python
os.rename("report.txt", "backup/report.txt")
```

### 📌 `Path.rename()` (pathlib 방식)

```python
from pathlib import Path

Path("hello.txt").rename("hello_backup.txt")
```

### 🧪 실습 8: 오래된 로그 파일 자동 정리

```python
from pathlib import Path

log_file = Path("log.txt")
if log_file.exists():
    log_file.unlink()
    print("이전 로그 파일 삭제 완료")
```

### 🧪 실습 9: 결과 파일 백업하기

```python
from pathlib import Path

result = Path("data.txt")
if result.exists():
    result.rename("data_backup.txt")
    print("파일 이름 변경 완료")
```

---

## 🧾 6-8. 파일 복사, 이동, 삭제, 압축 (`shutil` 모듈)

### 📌 `shutil` 모듈이란?

> 파일과 폴더를 **복사, 이동, 삭제, 압축**할 수 있게 해주는 유틸리티 모듈입니다.

## ✅ 1. 파일 복사 – `shutil.copy()`

```python
import shutil

shutil.copy("source.txt", "backup/source_backup.txt")
```

- `"원본파일"`, `"대상경로/이름"`
- 대상 폴더가 없으면 에러 발생

### 📌 전체 폴더 복사 – `copytree()`

```python
shutil.copytree("original_folder", "copy_folder")
```

- 폴더 전체 + 내부 파일까지 복사
- `copy_folder`가 **미리 존재하면 에러**

> ⚠️ 이미 있는 폴더로 덮어쓰기 하려면 `dirs_exist_ok=True` (Python 3.8+)

```python
shutil.copytree("original", "copy", dirs_exist_ok=True)
```

## ✅ 2. 파일/폴더 이동 – `shutil.move()`

```python
shutil.move("data.txt", "archive/data.txt")
```

- 파일을 **이동 또는 이름 변경**
- 이미 있는 파일에 덮어쓰기 가능

## ✅ 3. 폴더 통째로 삭제 – `shutil.rmtree()`

```python
shutil.rmtree("temp_folder")
```

- `os.rmdir()`은 비어있는 폴더만 삭제 가능
- `shutil.rmtree()`는 **안의 내용까지 전부 삭제**

> ⚠️ 실수하면 복구 불가! 조심해서 사용하세요

## ✅ 4. 폴더 압축 – `shutil.make_archive()`

```python
shutil.make_archive("backup_folder", "zip", "output")
```

- `"파일이름"`, `"형식"`, `"압축할 폴더"`
- 위 코드는 `backup_folder.zip`을 만들어 `output/` 폴더 내용을 압축합니다.

### 🧪 실습 10: 오늘의 작업 파일 백업

```python
import shutil
from pathlib import Path

Path("backup").mkdir(exist_ok=True)
shutil.copy("result.txt", "backup/result_backup.txt")
```

### 🧪 실습 11: 폴더를 zip으로 압축

```python
import shutil

shutil.make_archive("project_backup", "zip", "project_files")
```

---

## 🧾 6-9. CSV 파일 읽고 쓰기 (`csv` 모듈)

### 📌 CSV란?

> **Comma-Separated Values**: 콤마(,)로 구분된 텍스트 파일

예: `students.csv`

```
이름,나이,성적
홍길동,20,90
이몽룡,19,85
성춘향,21,95
```

- 엑셀에서 열면 **표처럼** 보임
- 텍스트 편집기에서는 `,`로 구분된 데이터

## ✅ 1. CSV 파일 쓰기 (`csv.writer`)

```python
import csv

with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["이름", "나이", "성적"])
    writer.writerow(["홍길동", 20, 90])
    writer.writerow(["이몽룡", 19, 85])
    writer.writerow(["성춘향", 21, 95])
```

- `writerow()` : 한 줄씩 쓰기
- `newline=""` : 윈도우에서 줄바꿈이 2번 되는 문제 방지

## ✅ 2. CSV 파일 읽기 (`csv.reader`)

```python
import csv

with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

출력:

```
['이름', '나이', '성적']
['홍길동', '20', '90']
['이몽룡', '19', '85']
...
```

> 결과는 **리스트**로 읽힘 (숫자도 문자열로 읽힘)

## ✅ 3. 딕셔너리 방식으로 읽기 (`csv.DictReader`)

```python
import csv

with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["이름"], row["성적"])
```

출력:

```
홍길동 90
이몽룡 85
성춘향 95
```

- 각 행을 **딕셔너리 형태로 반환**함 (`row["열이름"]`)

### 🧪 실습 12: 학생 성적표 CSV로 저장

```python
import csv

data = [
    ["이름", "과목", "점수"],
    ["홍길동", "수학", 90],
    ["이몽룡", "영어", 85],
    ["성춘향", "국어", 95],
]

with open("scores.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

### 🧪 실습 13: 출석부 불러와 리스트 만들기

```python
import csv

with open("attend.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # 헤더 건너뛰기
    names = [row[0] for row in reader]

print("출석한 학생:", names)
```

---

## 🧾 6-10. 실습 프로젝트 ① – 일기 저장기

### 🎯 목표

- 사용자가 입력한 내용을 **날짜별 파일**로 저장
- `with` 문, `open()`, `datetime` 사용

### ✅ 예제 코드

```python
from datetime import datetime

# 1. 오늘 날짜로 파일 이름 만들기
today = datetime.now().strftime("%Y-%m-%d")
file_name = f"diary_{today}.txt"

# 2. 사용자에게 일기 입력 받기
diary = input("오늘 하루를 한 줄로 정리해보세요:\n")

# 3. 파일에 저장
with open(file_name, "a", encoding="utf-8") as f:
    f.write(diary + "\n")

print(f"✅ '{file_name}' 파일에 일기가 저장되었습니다.")
```

### 💡 확장 아이디어

- `diary/` 폴더를 자동 생성하여 보관

```python
from pathlib import Path

Path("diary").mkdir(exist_ok=True)
file_path = Path("diary") / f"diary_{today}.txt"
```

---

## 🧾 6-11. 실습 프로젝트 ② – 출석부 분석기

---

### 🎯 목표

- CSV로 저장된 출석부를 불러와서
- 출석 인원 수 세기, 특정 학생 출석 여부 확인

---

### ✅ 예제 출석부 파일 (attend.csv)

```
이름,출석여부
홍길동,1
이몽룡,0
성춘향,1
```

---

### ✅ 예제 코드

```python
import csv

filename = "attend.csv"
attended = []

with open(filename, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["출석여부"] == "1":
            attended.append(row["이름"])

print("출석한 학생 수:", len(attended))
print("출석 명단:", attended)
```

---

### 🧪 추가 기능: 이름 검색 기능

```python
name = input("검색할 이름: ")
if name in attended:
    print(f"{name}님은 출석했습니다.")
else:
    print(f"{name}님은 결석했습니다.")
```

---

## 🎉 6장 마무리 요약

| 기능                         | 예시 도구                                |
| ---------------------------- | ---------------------------------------- |
| 텍스트 파일 쓰기/읽기        | `open()`, `with`, `write()`, `read()`    |
| 폴더 다루기                  | `os`, `pathlib`                          |
| 파일 복사/이동/삭제/압축     | `shutil`                                 |
| 표 형식 데이터 저장/불러오기 | `csv.writer`, `csv.reader`, `DictReader` |
