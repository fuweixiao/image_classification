from flask import Flask, render_template, request
import os, sys
import uuid

app = Flask(__name__)
@app.route('/')
def loadpage():
    return render_template('index.tmpl')

@app.route('/upload', methods = ['POST']) 
def upload_file():
    if request.method == 'POST':
	f = request.files["file"]
	print(f)
        path = '/home/fwx/fbcunn_imagenet/imagenet_raw_images/demo/val/other/demo.jpg'
	f.save(path)
	name = str(uuid.uuid4())
	os.system('cp ' + path + ' static/' + name + '.jpg')
	f.close()
	cmd = 'th /home/fwx/workspace/image_classification/binary_classification/main.lua'
	os.system(cmd)
	f = open('result/result.txt')
	res = f.readline()
	return render_template('index.tmpl', name = 'static/' + name + '.jpg', result = res)

if __name__ == '__main__':
    app.debug = True;
    app.run('0.0.0.0', 3000)
	
