from selenium import webdriver  #WebDriverはブラウザを操作するためのAPIを公開するモジュール
from selenium.webdriver.common.by import By #Byはクリックや入力が行えるようになるモジュール
from selenium.webdriver.support.ui import WebDriverWait #WebDriverWaitは任意のHTML要素が特定の状態になるまで待機させるモジュール
from selenium.webdriver.support import expected_conditions as EC #ある特定の状態になったのかなどが判断するモジュール
from selenium.common.exceptions import TimeoutException #読み込みに失敗した際の対応を書けるモジュール
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time #sleep(時間)で待機時間が書けるモジュール
import os #OSに依存しているディレクトリ操作などができるようになるモジュール
import pprint #リストの要素ごとに改行してくれるモジュール 
import json #jsonファイルを扱うためのモジュール
from bs4 import BeautifulSoup as BF #html要素をparseしてくれるモジュール
import requests
import pymysql
from select_data import select_capital
from select_data import select_employee
from select_data import select_listing
from select_data import select_sales
from select_data import select_business_type
from get_scrap_data import get_needs_data
from get_job_kind_data import get_job_kind_code
from get_pref_data import get_pref_data_code
from change_needs_data import change_needs_code
from return_first_needs_data import return_first_needs_code

#lambda_handlerはlambdaに設定されているトリガーが満たしたときに実行される関数名
def lambda_handler(event, context): #eventの中にトリガーとなったイベント情報が入る。

    get_needs_data()
    jj = json.loads(get_needs_data())
    print(jj)
    key1 = jj[0]['jobkind']
    key2 = jj[0]['prefectures']
    key3 = jj[0]['page']
    print(key1)
    print(key2)
    print(key3)

    get_job_kind_code()
    json_job_code = json.loads(get_job_kind_code())
    print(json_job_code)
    # job_code = json_job_code[key1]['code']

    get_pref_data_code()
    json_pref_code = json.loads(get_pref_data_code())
    print(json_pref_code)
    # pref_code = json_pref_code[key2]['code']

    #ブラウザ設定
    options = webdriver.ChromeOptions() #webdriverの起動
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    # options.add_argument("--hide-scrollbars")
    options.add_argument("--single-process")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--window-size=2000x3500")
    options.add_argument("--no-sandbox")
    options.add_argument("--homedir=/tmp")
    options.add_argument("--disable-dev-shm-usage") #メモリ不足でクラッシュするので追加
    options.binary_location = "/opt/python/bin/headless-chromium"

 

    
    #ブラウザを定義。
    driver = webdriver.Chrome(
        "/opt/python/bin/chromedriver",
        options = options,
        # desired_capabilities=capabilities
    )
    wait = WebDriverWait(driver=driver, timeout=15)


 

    #ログイン情報
    url = "---" #スクレーピング先のURL。
    email = "------"  #メールアドレス
    pas = "-------" #左辺をpassにするとpassは予約語なのでエラー　パスワードを入力。


    #URLにアクセス
    driver.get(url)
    wait.until(EC.presence_of_all_elements_located)


    html = driver.find_element(By.XPATH, "html[1]/body/div[2]/div/div/div/form/div/div[1]/div[1]/input[@id='login_username']")

 

    #データ入力フォームの要素を取得
    email_input = driver.find_element(By.ID, "login_username")
    pas_input = driver.find_element(By.ID, "login_password")
    button = driver.find_element(By.ID, "login_submit")

 

    #実際にログイン
    email_input.send_keys(email) #send_keysはキーボード入力をさせるメソッド。element.send_keys("入力値")
    pas_input.send_keys(pas)
    button.click() #clickメソッド　element.clickで要素をクリック。

    print("ログイン！！！")

 

    wait.until(EC.presence_of_all_elements_located)

    #リスト作成ページに飛ぶ　hrefになっているので。
    url2 = '---' //ログイン後に飛んで欲しいページ
    driver.get(url2) #postでurl2にアクセスしているのでpostで送信。
    wait.until(EC.presence_of_all_elements_located)

    #業種コード
    for num1 in range(key1, 95):
        key4 = json_job_code[num1]['code']
        print(key4)
        #市区町村数
        for num2 in range(key2, 1772):
            key5 = json_pref_code[num2]['code']
            print(key5)
            #ページ数
            for num3 in range(key3, 20):
                print(num3)
                url3 = '---?gyoshu_facet%5B%5D=' + str(key4) + '&citycode%5B%5D=' + str(key5) +'&free_word=&count=100&page=' + str(num3)
                driver.get(url3)
                print(driver.current_url)
                # print(driver.page_source)
                data = {}
                for num in range(1, 101):
                    if(len(driver.find_elements(By.XPATH, "//body/div/div[@id='member']/div/table/tbody/tr[{0}]/td[1]".format(num))) > 0):
                        data['data'] = driver.find_element(By.XPATH, "//body/div/div[@id='member']/div/table/tbody/tr/td")
                        data1 = data['data']
                        data2 = str(data1.text)
                        print(data2)
                        if(data2 != "検索結果はありません。"):
                            wait.until(EC.visibility_of_element_located((By.XPATH, "//body/div/div[@id='member']/div/table/tbody/tr[1]/td[1]/a")))
                            datas = {}
                            datas['company'] = driver.find_element(By.XPATH, "//body/div/div[@id='member']/div/table/tbody/tr[{0}]/td[1]".format(num))
                            datas['company_url'] = driver.find_element(By.XPATH, "//body/div/div[@id='member']/div/table/tbody/tr[{0}]/td[1]/a".format(num)).get_attribute('href')
                            datas['address'] = driver.find_element(By.XPATH, "//div/div/table/tbody/tr[{0}]/td[2]".format(num))
                            datas['tel_number'] = driver.find_element(By.XPATH, "//div/div/table/tbody/tr[{0}]/td[3]".format(num))
                            datas['job_kind'] = driver.find_element(By.XPATH, "//div/div/table/tbody/tr[{0}]/td[4]".format(num))
                            datas['capital'] = driver.find_element(By.XPATH, "//div/div/table/tbody/tr[{0}]/td[5]".format(num))
                            datas['employee'] = driver.find_element(By.XPATH, "//div/div/table/tbody/tr[{0}]/td[6]".format(num))
                            datas['turnover'] = driver.find_element(By.XPATH, "//div/div/table/tbody/tr[{0}]/td[7]".format(num))
                            datas['listing'] = driver.find_element(By.XPATH, "//div/div/table/tbody/tr[{0}]/td[8]".format(num))
                            datas['establish'] = driver.find_element(By.XPATH, "//div/div/table/tbody/tr[{0}]/td[9]".format(num))
                            datas['search'] = driver.find_element(By.XPATH, "//div/div/table/tbody/tr[{0}]/td[10]/a".format(num)).get_attribute('href')
                            datas['mail'] = driver.find_element(By.XPATH, "//div/div/table/tbody/tr[{0}]/td[11]".format(num))

                            #データを整形
                            company = datas['company']
                            company_url = datas['company_url']
                            address = datas['address']
                            tel_number = datas['tel_number']
                            job_kind = datas['job_kind']
                            capital = datas['capital']
                            employee = datas['employee']
                            turnover = datas['turnover']
                            listing = datas['listing']
                            establish = datas['establish']
                            search = datas['search']
                            mail = datas['mail']

                            #オブジェクトなので文字列に変換
                            company_value = str(company.text)
                            address_value = str(address.text).split()
                            if address.text[0] != '〒':
                                address_value2 = address_value
                                address_value1 = 'None'
                            else:
                                address_value1 = address_value[0]
                                address_value2 = address_value[1]
                            tel_number_value = str(tel_number.text).split()
                            job_kind_value = str(job_kind.text)
                            capital_value = str(capital.text)
                            employee_value = str(employee.text)
                            turnover_value = str(turnover.text)
                            if "未上場" == str(listing.text):
                                listing_value = 'None'
                                market = None
                                code = None
                            else:
                                listing_value = str(listing.text).split()
                                market = listing_value[0]
                                code = listing_value[1]
                            establish_value = str(establish.text)
                            mail_value = str(mail.text)

                            select_capital(capital_value)
                            capital_id = select_capital(capital_value)
                            select_employee(employee_value)
                            employee_id = select_employee(employee_value)
                            select_sales(turnover_value)
                            sales_id = select_sales(turnover_value)
                            select_listing(listing_value)
                            market_id = select_listing(listing_value)
                            select_business_type(job_kind_value)
                            business_type_id = select_business_type(job_kind_value)

                            # print(num)
                            # print(num2)

                            try:
                                db = pymysql.connect(
                                    db='----',
                                    user='-----',
                                    passwd='-----',
                                    host='------'
                                )
                                cursor = db.cursor()
                                print('DB connection successed')
                            except pymysql.Error as e:
                                print('db.Error: ', e)
                                print('DB connection failed')

                            #支店会社名で新規登録なのか違うのかで場合分け
                            name_result = cursor.execute('select name from company WHERE branch_name=%s AND name=%s', (company_value[1], company_value[0]))

                            if (0 == name_result):
                                print("新規登録")
                                try:
                                    sql = """INSERT INTO company(name, branch_name, url, addr1, addr2, tel, fax, business_type, capital, employee, sales, market, code, establish, search_url, email)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                                    cursor.execute(sql, (
                                        company_value[0], company_value[1], company_url, address_value1, address_value2, tel_number_value[0], tel_number_value[1], business_type_id, capital_id, employee_id, sales_id, market_id, code, establish_value, search, mail_value))
                                    db.commit()
                                    print('データベース登録に成功しました')
                                except pymysql.Error as e:
                                    print('db.Error: ', e)
                                    print('DB connection failed')
                            else:
                                print("アップデート")
                                try:
                                    id_result = cursor.execute('select id from company WHERE branch_name=%s', company_value[1])
                                    sql = ("""
                                    UPDATE company
                                    SET name=%s, branch_name=%s, url=%s, addr1=%s, addr2=%s, tel=%s, fax=%s, business_type=%s, capital=%s, employee=%s, sales=%s, market=%s, code=%s, establish=%s, search_url=%s, email=%s
                                    WHERE id=%s
                                    """)
                                    params = (company_value[0], company_value[1], company_url, address_value1, address_value2, tel_number_value[0], tel_number_value[1], business_type_id, capital_id, employee_id, sales_id, market_id, code, establish_value, search, mail_value, id_result)
                                    cursor.execute(sql, params)
                                    db.commit()
                                    print('データベース更新に成功しました')
                                except pymysql.Error as e:
                                    print('db.Error: ', e)
                                    print('DB connection failed')
                    change_needs_code(num1, num2, num3)
    if(num1 == 94 and num2 == 1771):
        return_first_needs_code()
    print('スクレーピング終了')

    # ブラウザを閉じる。
    driver.close()

 


    return {
        'statusCode': 200,
        'headers': {},
        'body': '{"message": "success"}'
    }
