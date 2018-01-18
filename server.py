from keras.models import load_model
import matplotlib.pyplot as plt
import numpy
import cv2

from flask import Flask, jsonify, request, render_template
from base64 import decodestring
app = Flask(__name__)

@app.route('/', methods=['GET'])
def drawing():
    return render_template('canvas.html')

@app.route('/decode', methods=['POST'])
def decode():
    print(request.form['send'][31:])
    with open("test.png", "wb") as f:
        f.write(decodestring(str.encode(request.form['send'][31:])))

    img = cv2.imread('test.png', 0)
    img = img.reshape(img.shape[0], 28).astype('float32')
    img = img / 255

    model = load_model('models/mnist_model.h5')

    img = plt.imread('../writeup/test.png')
    lis = []
    count = 0
    for a in img:
        for b in a:
            lis.append(b[3])
            count += 1

    img = numpy.array(lis).astype('float32')
    themodel = load_model('../writeup/models/mnist_model.h5')
    themodel.predict(numpy.array([img]))


    return "Decoded"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
