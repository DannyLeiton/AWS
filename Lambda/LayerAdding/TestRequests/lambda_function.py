import requests

def lambda_function(event, context):
    response = requests.get('https://acloud.guru')
    if response:
        print('Success!')
    else:
        print('Error occurred')