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
@app.route('/index')
def index():
    return flask.render_template('index.html')

#prediction function
def PricePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,9)
    loaded_model = pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        prediction = PricePredictor(to_predict_list)
            
        return render_template("result.html", prediction=prediction)


# @app.route('/', methods=['GET', 'POST'])
# def main():
#     if flask.request.method == 'GET':
#         return(flask.render_template('main.html'))
#     if flask.request.method == 'POST':
#         temperature = flask.request.form['temperature']
#         humidity = flask.request.form['humidity']
#         windspeed = flask.request.form['windspeed']
#         input_variables = pd.DataFrame([[temperature, humidity, windspeed]],
#                                        columns=['temperature', 'humidity', 'windspeed'],
#                                        dtype=float)
#         prediction = model.predict(input_variables)[0]
#         return flask.render_template('main.html',
                                    #  original_input={'Temperature':temperature,
                                    #                  'Humidity':humidity,
                                    #                  'Windspeed':windspeed},
                                    #  result=prediction,
                                    #  )