import os
import boto3
import logging
from boto3.session import Session
from .config import Config as conf

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
loglevels = {
    "CRITICAL": logging.CRITICAL,
    "WARNING": logging.WARNING,
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "": logging.INFO
}
logger.setLevel(loglevels[os.getenv("LOG_LEVEL", "INFO")])

def _open_aws_session(aws_access_key_id=conf.AWS_KEY,
                      aws_secret_access_key=conf.AWS_SECRET,
                      aws_session_token=conf.AWS_TOKEN,
                      region_name=conf.AWS_REGION,
                      profile=conf.AWS_PROFILE):

    sess = Session(aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    aws_session_token=aws_session_token,
                    region_name=region_name,
                    profile_name=profile)
    return sess

def get_aws_client(service=None, 
                   aws_access_key_id=conf.AWS_KEY,
                   aws_secret_access_key=conf.AWS_SECRET,
                   aws_session_token=conf.AWS_TOKEN,
                   region_name=conf.AWS_REGION,
                   profile=conf.AWS_PROFILE):
    """
    Function to create AWS client instance with the chosen service (e.g. S3, SQS) - this is not an open connection.
    ====PARAM====
    aws_access_key_id: aws access key
    aws_secret_access_key: aws secret key
    region_name: aws region
    profile: aws profile to use, which will be fetched from ~/.aws/credentials

    ====RETURN====
    boto3 s3/sqs client object
    """
    service = service or 's3'
    if any([profile, aws_access_key_id, aws_secret_access_key]):
        sess = _open_aws_session(aws_access_key_id, aws_secret_access_key, aws_session_token, region_name, profile)
        return sess.client(service)
    return boto3.client(service)

def get_aws_resource(service=None, 
                   aws_access_key_id=conf.AWS_KEY,
                   aws_secret_access_key=conf.AWS_SECRET,
                   aws_session_token=conf.AWS_TOKEN,
                   region_name=conf.AWS_REGION,
                   profile=conf.AWS_PROFILE):
    """
    Function to create AWS resource instance with the chosen service (e.g. S3, SQS) - this is not an open connection.
    ====PARAM====
    aws_access_key_id: aws access key
    aws_secret_access_key: aws secret key
    region_name: aws region
    profile: aws profile to use, which will be fetched from ~/.aws/credentials

    ====RETURN====
    boto3 s3/sqs resource object
    """
    service = service or 's3'
    sess = _open_aws_session(aws_access_key_id, aws_secret_access_key, aws_session_token, region_name, profile)
    return sess.resource(service)