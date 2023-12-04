# import requests
# import json
# url = "https://a.klaviyo.com/api/v1/email-templates?page=0&count=150&api_key=pk_e282bb52aa8799bfe6355559c9453b9ead"

# headers = {"accept": "application/json"}

# response = requests.get(url, headers=headers)

# # print(response.text)
# # print(response)
# count = 0
# data = json.loads(response.text)
# # print(data['data'][1])
# for res in data['data']:
    
#     print("ID :", res['id'],",","Name :", res['name'])
#     count += 1
#     print(count)

import requests
import json

url = "https://a.klaviyo.com/api/v1/email-templates"
api_key = "pk_e282bb52aa8799bfe6355559c9453b9ead"

headers = {"accept": "application/json"}

page = 0  # Start with the first page
count = 500  # Number of records per page
countt = 0
while True:
    params = {"page": page, "count": count, "api_key": api_key}
    response = requests.get(url, headers=headers, params=params)
    data = json.loads(response.text)
    
    if not data['data']:
        break
    
    for res in data['data']:
        print("ID:", res['id'], ",", "Name:", res['name'])
        countt += 1
        print(countt)
    
    page += 1  # Move to the next page
