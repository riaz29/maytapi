from pprint import pprint
import re
from urllib import response
import requests
import json
BASE_URL = 'https://api.maytapi.com/api'

product_id='cb51a901-4e30-44dd-bf3b-a5ac615da0ca'
phone_id='25092'

headers = {
            "Content-Type": "application/json",
            "x-maytapi-key":"dc6f8283-1b15-411e-885e-b2fc0cac8cba"
        }
params={
        'limit':'100',
        'archived':'false',
        'associations':'contact',
        'properties':'hs_note_body'
    }
body_data= {
    "to_number": "923073869042",
    "type": "text",
    "message": "Hello Tahir!"
}


url='https://api.maytapi.com/api/product_id/phone_id/sendMessage'
response= requests.post(f"{BASE_URL}/{product_id}/{phone_id}/sendMessage", json=body_data,headers=headers)
res=response.json()
pprint(res)


