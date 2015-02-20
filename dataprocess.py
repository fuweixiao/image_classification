import json
import urllib
from pprint import pprint
json_data=open('pin.json')

data = json.load(json_data)
url = data["images"]["236x"]["url"]
strs = url.split(' ')
url = ""
for str in strs:
    url = url + str 
file_name = url.split('/')[-1]
urllib.urlretrieve (url, file_name)
print data["board"]["category"]
json_data.close()

