#indexテーブルからidを取得してメインテーブルに登録する値を決める用
from create_data import create_capital
from create_data import create_employee
from create_data import create_sales
from create_data import create_business_type
from create_data import create_market
import pymysql

 

def select_capital(capital_value):
    try:
        db = pymysql.connect(
            db='-----',
            user='-----',
            passwd='-----',
            host='-----'
        )
        cursor = db.cursor()
        print('DB connection successed')
    except pymysql.Error as e:
        print('db.Error: ', e)
        print('DB connection failed')
    #資本金
    capital_result = cursor.execute('SELECT id FROM capital WHERE name = %s', capital_value)
    if 0 == capital_result:
        create_capital(capital_value)

 

    capital_id = cursor.execute('select id from capital WHERE name=%s', capital_value)

    return capital_value

def select_employee(employee_value):
    try:
        db = pymysql.connect(
            db='-----',
            user='-----',
            passwd='-----',
            host='-----'
        )
        cursor = db.cursor()
        print('DB connection successed')
    except pymysql.Error as e:
        print('db.Error: ', e)
        print('DB connection failed')
    #従業員数
    employee_result = cursor.execute('select id from employee WHERE name = %s', employee_value)
    # print(employee_result)
    if 0 == employee_result:
        create_employee(employee_value)

 

    employee_id = cursor.execute('select id from employee WHERE name = %s', employee_value)

    return employee_id

def select_sales(turnover_value):
    try:
        db = pymysql.connect(
            db='-----',
            user='-----',
            passwd='-----',
            host='-----'
        )
        cursor = db.cursor()
        print('DB connection successed')
    except pymysql.Error as e:
        print('db.Error: ', e)
        print('DB connection failed')
    #売り上げ
    sales_result = cursor.execute('select id from sales WHERE name = %s', turnover_value)
    # print(sales_result)
    if 0 == sales_result:
        create_sales(turnover_value)

    sales_id = cursor.execute('select id from sales WHERE name=%s', turnover_value)

    return sales_id

def select_listing(listing_value):
    try:
        db = pymysql.connect(
            db='-----',
            user='-----',
            passwd='-----',
            host='-----'
        )
        cursor = db.cursor()
        print('DB connection successed')
    except pymysql.Error as e:
        print('db.Error: ', e)
        print('DB connection failed')
    #上場
    if listing_value == 'None':
        market = 'None'
    else:
        market = listing_value[0]
        market_result = cursor.execute('select id from market WHERE name=%s', market)
        if 0 == market_result:
            create_market(market)

    market_id = cursor.execute('select id from market WHERE name=%s', market)

    return market_id

def select_business_type(job_kind_value): 
    try:
        db = pymysql.connect(
            db='-----',
            user='-----',
            passwd='-----',
            host='-----'
        )
        cursor = db.cursor()
        print('DB connection successed')
    except pymysql.Error as e:
        print('db.Error: ', e)
        print('DB connection failed')
    #業種
    business_type_result = cursor.execute('select id from business_type WHERE name = %s', job_kind_value)
    if 0 == business_type_result:
        create_business_type(job_kind_value)

    business_type_id = cursor.execute('select id from business_type WHERE name = %s', job_kind_value)

    return business_type_id