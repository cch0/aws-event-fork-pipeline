import json

import pytest

from splitter import app


@pytest.fixture()
def kinesis_event():
    """ Generates Kinesis Event"""

    return {
  "invocationId": "dcd4ac4b-f92d-4b30-8639-b18150adb13e",
  "sourceKinesisStreamArn": "arn:aws:kinesis:us-west-2:484559884317:stream/activity",
  "deliveryStreamArn": "arn:aws:firehose:us-west-2:484559884317:deliverystream/activity-to-s3",
  "region": "us-west-2",
  "records": [
    {
      "recordId": "49607552066000566344891626412151406980683478788707713026000000",
      "approximateArrivalTimestamp": 1592886612275,
      "data": "ewoia2V5MSI6InZhbHVlMSIsCiJrZXkyIjoidmFsdWUyIgp9",
      "kinesisRecordMetadata": {
        "sequenceNumber": "49607552066000566344891626412151406980683478788707713026",
        "subsequenceNumber": 0,
        "partitionKey": "0623-02",
        "shardId": "shardId-000000000000",
        "approximateArrivalTimestamp": 1592886612275
      }
    },
    {
      "recordId": "49607552066000566344891626412395609996245633950717837314000000",
      "approximateArrivalTimestamp": 1592886612887,
      "data": "ewoia2V5MSI6InZhbHVlMSIsCiJrZXkyIjoidmFsdWUyIgp9",
      "kinesisRecordMetadata": {
        "sequenceNumber": "49607552066000566344891626412395609996245633950717837314",
        "subsequenceNumber": 0,
        "partitionKey": "0623-02",
        "shardId": "shardId-000000000000",
        "approximateArrivalTimestamp": 1592886612887
      }
    }
  ]
}

def test_lambda_handler(kinesis_event, mocker):

    ret = app.lambda_handler(kinesis_event, "")
    print(ret)

    assert len(ret["records"]) == 2
    assert ret["records"][0]["result"] == "Ok"
    assert ret["records"][0]["data"].endswith("Cg==")
