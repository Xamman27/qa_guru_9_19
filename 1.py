import requests
from test_api import base_url

response = requests.post(url=base_url, data={"name": "morpheus", "job": "master"})
print(response.json())