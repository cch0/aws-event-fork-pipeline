from __future__ import print_function

import base64


def lambda_handler(event, context):
    
    output = []

    for record in event['records']:
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': str(record['data'])+"Cg=="
        }

        output.append(output_record)

    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}
