#市区町村情報をjsonファイルにするためのプログラム
#lambda_functionと組み合わせて指定の箇所をスクレイピングしながらデータを作成s3保存を行なっている。
#いらない全域情報が47件取得される。またareaListという名前がつくのでVScodeで置き換えで一括削除した。
for k in range(1, 48):
    k = str(k)
    if(2 != len(str(k))):
        k = "0" + k
    driver.find_element(By.ID, "chk_ken" + k).click()
    time.sleep(10)
    for num in range(2, 200):
        if(len(driver.find_elements(By.XPATH, "//div/div/div[2]/ul/li[{0}]".format(num))) > 0):
            datas = {}
            datas['code'] = driver.find_element(By.XPATH, "//div/div/div[2]/ul/li[{0}]/label/input".format(num)).get_attribute('id')
            code = datas['code']
            code_value = str(code)
            json_dict += {
                    "code": code_value
            },
s3 = boto3.resource('s3')
bucket = '---'
key = '---' #ファイル名
json_data = json.dumps(json_dict)

#s3に接続
obj = s3.Object(bucket, key)
#s３にjson_dataの内容をファイル形式で保存。
obj.put(Body=json_data)
