import json
import urllib
import os

#set up input and output
inputpath =  '/home/smile/workspace/pinterest/data/pin_pins.json'
outputpath = '/home/smile/pinterest/'
dictfile = '/home/smile/workspace/image_classification/result-final.txt'
try:
    os.mkdir(outputpath)
except:
    pass

#read dictfile
dictionary = {}
lines = open(dictfile).readlines()
for line in lines:
    kvpair = line.split(',')
    key = kvpair[0]
    del kvpair[0]
    dictionary[key] = kvpair

#deal with useless lines which cannot be parsed
#lines = open(inputpath).readlines()
#for i in range(0, len(lines)):
#    if lines[i].find('ObjectId') != -1:
#        del lines[i]
#        i = i - 1
#    if lines[i].find('description') != -1 and lines[i].find('html') == -1:
#        del lines[i]
#        break
#open('pin.json', 'w').writelines(lines)

#parse json
json_file = open(inputpath)
json_data = json_file.readline(); 
while json_data:
    data = json.loads(json_data)
    #download and save images
    url = data["images"]["236x"]["url"]
    #strs = url.split(' ')
    #url = ""
    #for str in strs:
    #    url = url + str 
    file_name = url.split('/')[-1]
    
    category = data["board"]["category"]
    if category == None:
        category = "unknown"
    dirname = category
    if dictionary.has_key(category):
        for value in dictionary[category]:
            dirname = value.split('\n')[0]
            try:
                os.mkdir(outputpath + dirname)
            except:
                pass
            urllib.urlretrieve (url, outputpath + dirname + '/' + file_name)
    else:
        try:
            os.mkdir(outputpath + dirname)
        except:
            pass
        urllib.urlretrieve (url, outputpath + dirname + '/' + file_name)
    json_data = json_file.readline() 
    
json_file.close()

