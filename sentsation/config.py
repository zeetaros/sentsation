import os

class Config(object):
    TARGET_BUCKET = os.getenv("TARGET_BUCKET")
    AWS_KEY = os.getenv("AWS_KEY")
    AWS_SECRET = os.getenv("AWS_SECRET")
    AWS_TOKEN = getenv("AWS_TOKEN")
    AWS_REGION = getenv("AWS_REGION")
    AWS_PROFILE = getenv("AWS_PROFILE")
