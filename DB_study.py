import pymysql.cursors

# MySQL Connection 연결
conn = pymysql.connect(host='localhost',
                            user='root',
                            password='Rlanwjd67!',
                            db='sign_up',
                            charset='utf8')

# SELECT문 실행
try:
    # Cursor 객체 반환
    # cursor : control structure of database (실질적으로 SQL문을 수행, 결과를 가져오는 역할)
    # Default : Array based cursor (row 결과를 array(=tuple) 형태로)
    cursor = conn.cursor()

    # pymysql.cursor.DictSursor : Dictionary based cursor (row 결과를 Dictionary 형태로)
    # ex. cursor = conn.cursor(pymysql.cursor.DictSursor)

    # Cursor로 테이블 조회를 위한 SQL문 실행
    cursor.execute("SELECT * FROM `user_signup`")

    # Data Fetch
    rows = cursor.fetchall()
    
    # 전체 rows 출력
    print(rows)

# Connection 종료
finally:
    cursor.close()
    conn.close()