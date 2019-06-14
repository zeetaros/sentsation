import boto3
from boto3.session import Session as S3Session
from .config import Config

def get_s3_client(token=None):
    if token:
        sess = S3Session(aws_access_key_id=token['Credentials']['AccessKeyId'],
                aws_secret_access_key=token['Credentials']['SecretAccessKey'],
                aws_session_token=token['Credentials']['SessionToken'])
    else:
        sess = S3Session(aws_access_key_id=Config.AWS_KEY,
                aws_secret_access_key=Config.AWS_SECRET)
    return sess.client('s3')

def get_s3_resource(token=None):
    if token:
        sess = S3Session(aws_access_key_id=token['Credentials']['AccessKeyId'],
                aws_secret_access_key=token['Credentials']['SecretAccessKey'],
                aws_session_token=token['Credentials']['SessionToken'])
    else:
        sess = S3Session(aws_access_key_id=Config().AWS_KEY,
                aws_secret_access_key=Config().AWS_SECRET)
    return sess.resource('s3')

# aws s3 presign s3://awsexamplebucket/test2.txt --expires-in 60*15

# https://stackoverflow.com/questions/2677317/how-to-read-remote-video-on-amazon-s3-using-ffmpeg
    