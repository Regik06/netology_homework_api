import requests
from pprint import pprint

url = 'https://api.stackexchange.com/2.3/questions?fromdate=1674432000&todate=1674604800&order=desc&sort=activity&tagged=%27Python%27&site=stackoverflow'
response = requests.get(url)
a = dict(response.json())
question_dict = {}
for k,v in a.items():
    if 'items' in k:
        for j in v:
            question_dict[j['title']] = j['link']
pprint(question_dict)
