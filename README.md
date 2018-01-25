## Explanation
This project takes images drawn in html5 canvas and submits them through a simple
dense neural network trained on the MNIST dataset. I will be swapping out the model to a more mature convolutional neural network (CNN) that should perform much better than the current network.

## Installation Instructions
I use [miniconda](https://conda.io/miniconda.html) for Python 3.6 to run the project.

Once you have miniconda installed, go to the project directory and run
```
conda env create -f environment.yml
```
Finally run:
```
source activate kera (or whatever you named your env)
python server.py
```
You'll be able to see the simple Flask app running on *localhost:5000*


## Using the simple app
To use, simply draw a number in the canvas and click the Submit button. Below the buttons,
there is a *<div>* that will populate with the given prediction. Currently the prediction is trained on handwritten digits and not digits drawn in html5 canvas so you may need to exaggerate your strokes to get accurate guesses. Eventually there will be an ability to train using the images made on the website and not just the MNIST files that keras trains by default.

## Additional Notes

Due to a weird [issue](https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python) with macos and matplotlib, you will have to add this text to a file at your root directory.
```
Name of file: ~/.matplotlib/matplotlibrc

Paste the following into the document

backend: TkAgg
```
