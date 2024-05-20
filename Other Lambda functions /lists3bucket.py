#add iam roles to the lamda-s3-role and give s3 permissions

import _json
import boto3

s3 = boto3.resoruce9('s3')

def lamda_handler(event,context):
    bucker_list= []
    for bucket in s3.buckets.all():
        print (bucket.name)
        bucket.list.append(bucket.name)
    return{
        'statusCode':200,
        'body': bucker_list

    }