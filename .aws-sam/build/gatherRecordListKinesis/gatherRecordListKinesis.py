import datetime
import logging
import base64
import json
import boto3
import os


logger = logging.getLogger()
logger.setLevel(logging.INFO)
client = boto3.client('stepfunctions')
STATE_MACHINE_ARN = os.getenv("STATE_MACHINE_ARN")


def get_kinesis_records(evt):
    logger.info(f"Get {len(evt['Records'])} Kinesis_records from event")
    records = evt['Records']
    logger.info(f"Processing a batch of {len(records)} records")

    record_list = []
    for r in records:
        payload_byte = (r["kinesis"]["data"]).encode('utf-8')
        payloadstr = ((base64.b64decode(payload_byte)).decode('utf-8'))
        pstr = payloadstr.replace("'", '"')
        payload = json.loads(pstr)
        record_list.append(payload)
    return(record_list)




def lambda_handler(event, context):
    ts = datetime.datetime.now()
    logger.info("===================================================================================================")
    logger.info(f"**********               {ts}")
    logger.info(f"eeeeeeeeeeeeeeeeeeeeee {event}")
    logger.info("BEGIN Kinesis gather Records Handler")
    data = {'Data': get_kinesis_records(event)}
    record_list_str = json.dumps(data)

    # Execute the state machine asynchronously
    sf_name = f"StudyMgmt{datetime.datetime.now()}".replace(' ','').replace('-','').replace(':','').replace('.','')
    logger.info(f"State Machine ARN = {STATE_MACHINE_ARN}")
    logger.info(f"RecordList = {record_list_str}")
    response = client.start_execution(
        stateMachineArn=STATE_MACHINE_ARN,
        name=sf_name,
        input=record_list_str
    )
    logger.info(f"records={record_list_str}")
    logger.info(f"response = {response}")
    a = {
        "statusCode": 200,
        "errorMessage": "Success",
        "body": {
            "records": record_list_str
        }
    }
    ts = datetime.datetime.now()
    logger.info(f"END CONSUMER function complete - {a}     - Finish time = {ts}")
    logger.info("----------------------------------------------------------------------------------------------------")
    return a

