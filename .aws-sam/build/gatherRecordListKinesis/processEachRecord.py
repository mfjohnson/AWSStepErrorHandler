import datetime
import logging
import base64
import json
import boto3
import os


logger = logging.getLogger()
logger.setLevel(logging.INFO)

# TODO Setup Exception based error and validate retry
# TODO Setup error code based error and validate retry
def lambda_handler(event, context):
    logger.info(f"Processing {type(event)} Event = {event}")
