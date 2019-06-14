import os

class Config(object):
    S3_BUCKET = os.getenv("S3_BUCKET")
    AWS_KEY = os.getenv("AWS_KEY")
    AWS_SECRET = os.getenv("AWS_SECRET")
