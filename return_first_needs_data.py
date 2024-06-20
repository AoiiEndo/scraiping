#全ての業種で全ての市区町村をスクレイピングし終わったら最初に戻る。
import boto3
import json

def return_first_needs_code():
    s3 = boto3.resource('s3')
    bucket = '-----'
    key = '---' //ファイル名

    json_dict = {
        "jobkind": 1,
        "prefectures": 1,
        "page": 1
    },
    json_data = json.dumps(json_dict)
    obj = s3.Object(bucket, key)
    obj.put(Body=json_data)
    return()
