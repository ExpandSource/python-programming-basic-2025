# 수정된 MySQL 연결 코드 - 기본 연결 예제
import mysql.connector
from mysql.connector import Error

# 연결 변수를 미리 None으로 초기화
conn = None

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="비밀번호",
        database="pyuserdb",
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )
    
    if conn.is_connected():
        print("✅ MySQL 연결 성공!")
        
        # 현재 연결된 DB 확인
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        row = cursor.fetchone()
        print(f"현재 연결된 DB: {row[0]}")
        cursor.close()

except Error as e:
    print(f"❌ MySQL 연결 실패: {e}")x``

finally:
    # conn이 None이 아니고 연결되어 있는 경우에만 종료
    if conn is not None and conn.is_connected():
        conn.close()
        print("🔌 연결 종료")

print("=" * 50)

# 수정된 데이터 저장 예제
conn = None
cursor = None

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="비밀번호",
        database="pyuserdb",
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )
    
    if conn.is_connected():
        print("✅ DB 연결 성공")

        name = input("이름 입력: ")
        email = input("이메일 입력: ")
        age = int(input("나이 입력: "))

        cursor = conn.cursor()
        sql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
        values = (name, email, age)
        
        cursor.execute(sql, values)
        conn.commit()
        
        print("✅ 저장 완료!")

except Error as e:
    print(f"❌ MySQL 에러: {e}")
    # 에러 발생 시 롤백
    if conn is not None and conn.is_connected():
        conn.rollback()
        print("🔄 트랜잭션 롤백")

except ValueError as e:
    print(f"❌ 입력값 오류: {e}")

except Exception as e:
    print(f"❌ 예상치 못한 오류: {e}")

finally:
    # cursor와 conn을 안전하게 종료
    if cursor is not None:
        cursor.close()
    if conn is not None and conn.is_connected():
        conn.close()
        print("🔌 연결 종료")

print("=" * 50)

# with문을 사용한 더 안전한 방법
conn = None

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="비밀번호",
        database="pyuserdb",
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )
    
    if conn.is_connected():
        print("✅ DB 연결 성공")
        
        # with문으로 cursor 자동 관리
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            
            print("\n📋 저장된 사용자 목록:")
            for row in rows:
                print(f"ID: {row[0]}, 이름: {row[1]}, 이메일: {row[2]}, 나이: {row[3]}")

except Error as e:
    print(f"❌ MySQL 에러: {e}")

except Exception as e:
    print(f"❌ 예상치 못한 오류: {e}")

finally:
    if conn is not None and conn.is_connected():
        conn.close()
        print("🔌 연결 종료")

print("=" * 50)

# 함수로 만든 안전한 연결 패턴
def get_db_connection():
    """안전한 DB 연결 함수"""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="비밀번호",
            database="pyuserdb",
            charset='utf8mb4',
            collation='utf8mb4_general_ci'
        )
        return conn
    except Error as e:
        print(f"❌ 연결 실패: {e}")
        return None

def safe_db_operation():
    """안전한 DB 작업 함수"""
    conn = get_db_connection()
    
    if conn is None:
        print("❌ 데이터베이스 연결에 실패했습니다.")
        return
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM users")
            count = cursor.fetchone()[0]
            print(f"📊 총 사용자 수: {count}명")
            
    except Error as e:
        print(f"❌ 쿼리 실행 오류: {e}")
        
    finally:
        if conn.is_connected():
            conn.close()
            print("🔌 연결 종료")

# 함수 실행
safe_db_operation()