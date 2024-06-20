#新たなカラムを作成するプログラム
import pymysql

#資本金の新たなデータ作成関数。
def create_capital(capital_value):
    try:
        db = pymysql.connect(
            db='----',
            user='----',
            passwd='-----',
            host='-----'
        )
        cursor = db.cursor()
    except pymysql.Error as e:
        print('db.Error: ', e)
        print('DB connection failed')

 

    print('DB connection successed')

    sql = """INSERT INTO capital(name, created_at)
            VALUES (%s, now())"""
    try:
        cursor.execute(sql, (
            capital_value))
        db.commit()
        print('資本金データ作成に成功')
    except:
        print('資本金データ作成に失敗')
    return capital_value

#従業員数の新たなデータ作成関数。
def create_employee(employee_value):
    try:
        db = pymysql.connect(
            db='-----',
            user='----',
            passwd='----',
            host='----'
        )
        cursor = db.cursor()
    except pymysql.Error as e:
        print('db.Error: ', e)
        print('DB connection failed')
    print('DB connection successed')

    sql = """INSERT INTO employee(name, created_at)
            VALUES (%s, now())"""
    try:
        cursor.execute(sql, (
            employee_value))
        db.commit()
        print('従業員データ作成に成功')
    except:
        print('従業員データ作成に失敗') 
    return employee_value

 

#売り上げの新たなデータ作成関数。
def create_sales(turnover_value):
    try:
        db = pymysql.connect(
            db='----',
            user='----',
            passwd='----',
            host='-----'
        )
        cursor = db.cursor()
    except pymysql.Error as e:
        print('db.Error: ', e)
        print('DB connection failed')
    print('DB connection successed')

    sql = """INSERT INTO sales(name, created_at)
            VALUES (%s, now())"""
    try:
        cursor.execute(sql, (
            turnover_value))
        db.commit()
        print('売り上げデータ作成に成功')
    except:
        print('売り上げデータ作成に失敗') 
    return turnover_value

 

#上場の新たなデータ作成関数
def create_market(market):
    try:
        db = pymysql.connect(
            db='----',
            user='-----',
            passwd='-----',
            host='-----'
        )
        cursor = db.cursor()
    except pymysql.Error as e:
        print('db.Error: ', e)
        print('DB connection failed')
    print('DB connection successed')

    sql = """INSERT INTO market(name, created_at)
            VALUES (%s, now())"""
    try:
        cursor.execute(sql, (
            market))
        db.commit()
        print('上場データ作成に成功')
    except:
        print('上場データ作成に失敗') 
    return market


 

#業種の新たなデータ作成関数。
def create_business_type(job_kind_value):
    try:
        db = pymysql.connect(
            db='----',
            user='----',
            passwd='----',
            host='-----'
        )
        cursor = db.cursor()
    except pymysql.Error as e:
        print('db.Error: ', e)
        print('DB connection failed')
    print('DB connection successed')

    sql = """INSERT INTO business_type(name, created_at)
            VALUES (%s, now())"""
    try:
        cursor.execute(sql, (
            job_kind_value))
        db.commit()
        print('業種データ作成に成功')
    except:
        print('業種データ作成に失敗') 
    return job_kind_value