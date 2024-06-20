#業種コードをjsonファイルにしてs3に保存したプログラム
#lambda_functionと組み合わせて指定の箇所をスクレイピングしながらデータを作成している。
json_dict = {
    "code": "job_kind"
},
for k in range(1, 20):
    pas = "//div/div/form/table/tbody/tr["+str(k)+"]"
    for num in range(1, 17):
        if(len(driver.find_elements(By.XPATH, pas + "/td/ul/li[{0}]".format(num))) > 0):
            datas = {}
            datas['code'] = driver.find_element(By.XPATH, pas + "/td/ul/li[{0}]/label/input".format(num)).get_attribute('value')
            code = datas['code']
            code_value = str(code)
            json_dict += {
                    "code": code_value
            },
s3 = boto3.resource('s3')
bucket = '----'
key = '---' #ファイル名
json_data = json.dumps(json_dict)

#s3に接続
obj = s3.Object(bucket, key)
#s３にjson_dataの内容をファイル形式で保存。
obj.put(Body=json_data)
