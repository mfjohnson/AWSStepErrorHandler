import logging
import random

from random import randrange
print(randrange(10))

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# TODO Setup Exception based error and validate retry
# TODO Setup error code based error and validate retry
def lambda_handler(event, context):
    statusCode = 200
    statusMsg = "Successfully processed row"
    logger.info(f"Processing {type(event)} Event = {event}")
    logger.info(f"*** context = {context}")

    if event is not None:
        r = random.randrange(5)

        if event['iteration'] == 0 and r<3:
#            statusCode = 420
            statusMsg = f"Error encountered {event}"
            raise Exception(statusMsg)

    result = {
        "statusCode": statusCode,
        "errorMessage": statusMsg,
        "body": {
            "record": event
        }
    }
    logger.info(result)
    return result
