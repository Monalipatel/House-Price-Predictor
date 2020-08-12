#importing libraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
def index():
    return render_template('index.html')

#prediction function
def PricePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,9)
    loaded_model = pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/result',methods = ['POST'])   
def result():
    if request.method == 'POST':
        print(request.form)
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        prediction = PricePredictor(to_predict_list)
        print(to_predict_list)
        return flask.render_template("result.html", prediction=to_predict_list)

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()