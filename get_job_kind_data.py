#job_kindの種類のデータの入ったjsonファイル
import boto3
import json

def get_job_kind_code():
    s3 = boto3.resource('s3')
    bucket = '-----'
    key = '---' //ファイル名
    obj = s3.Object(bucket, key)
    json_object = obj.get()
    json_jobCode = json_object['Body'].read().decode('utf-8')
    return json_jobCode
