#どこからスクレイピングを始めれば良いかを記述しているjsonファイルデータを取得
import boto3
import json

def get_needs_data():
    s3 = boto3.resource('s3')
    bucket = '-----'
    key = '---' //ファイル名
    obj = s3.Object(bucket, key)
    json_object = obj.get()
    json_data = json_object['Body'].read().decode('utf-8')
    return json_data
