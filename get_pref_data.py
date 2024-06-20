#市区町村jsonデータ取得用
import boto3
import json 

def get_pref_data_code():
    s3 = boto3.resource('s3')
    bucket = '-----'
    key = '---' //ファイル名
    obj = s3.Object(bucket, key)
    json_object = obj.get()
    json_pref = json_object['Body'].read().decode('utf-8')
    return json_pref
