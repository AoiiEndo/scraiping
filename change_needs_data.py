#最大の20ページまでスクレイピングしたら次のデータを最初に読まれるjsonファイルに上書き
import boto3
import json

def change_needs_code(num1, num2, num3):
    s3 = boto3.resource('s3')
    bucket = '-----'
    key = 'scraping_needs_data.json'

    if(num3 == "20"):
        num3 = 1

    json_dict = {
        "jobkind": num1,
        "prefectures": num2,
        "page": num3
    },
    json_data = json.dumps(json_dict)
    obj = s3.Object(bucket, key)
    obj.put(Body=json_data)
    return()