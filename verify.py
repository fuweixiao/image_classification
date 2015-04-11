import os
import Image
path = '/home/test/fbcunn_imagenet/imagenet_raw_images/technology/train/technology/'
f = open('/home/test/fbcunn_imagenet/imagenet_raw_images/technology/train.txt', 'w')
for filename in os.listdir(path):
    try:
    	im = Image.open(path + filename)
	im.verify()
    except:
	f.write(filename + '\n')
f.close()
