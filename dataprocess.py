import json
import urllib
import os

#set up input and output
inputpath =  'orig.json'
outputpath = '/home/smile/pinterest/'
try:
    os.mkdir(outputpath)
except:
    pass



#deal with useless lines which cannot be parsed
lines = open(inputpath).readlines()
for i in range(0, len(lines)):
    if lines[i].find('ObjectId') != -1:
        del lines[i]
        i = i - 1
    if lines[i].find('description') != -1 and lines[i].find('html') == -1:
        del lines[i]
        break
open('pin.json', 'w').writelines(lines)

#parse json
json_data=open('pin.json')
data = json.load(json_data)

#download and save images
url = data["images"]["236x"]["url"]
strs = url.split(' ')
url = ""
for str in strs:
    url = url + str 
file_name = url.split('/')[-1]
category = data["board"]["category"]
try:
    os.mkdir(outputpath + category)
except:
    pass
urllib.urlretrieve (url, outputpath + category + '/' + file_name)
json_data.close()

