#importing libraries
import os
import numpy as np
import flask
import joblib
from flask import Flask, render_template, request

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
def index():
    return render_template('index.html')

#prediction function
def PricePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,8)
    loaded_model = joblib.load("model.joblib")
    X_scaler = joblib.load("X_scaler.joblib")
    y_scaler = joblib.load("y_scaler.joblib")
    X_scaled = X_scaler.transform(to_predict)
    result = loaded_model.predict(X_scaled)
    result_unscaled = y_scaler.inverse_transform(result)
    final_prediction =  round(result_unscaled[0])
    final_prediction = "${:,.0f}".format(final_prediction)
    
    return final_prediction

@app.route('/result',methods = ['GET','POST'])   
def result():
    if request.method == 'POST':
        overall_quality = request.form['overall-quality']
        ground_area=request.form['ground-area']
        second_floor_area=request.form['second-floor-area']
        basement_area=request.form['basement-area']
        first_floor_area=request.form['first-floor-area']
        lot_area=request.form['lot-area']
        year_built=request.form['year-built']
        garage_cars=request.form['garage-cars']
   
        to_predict_list = [overall_quality,ground_area,second_floor_area,basement_area,first_floor_area,lot_area,year_built,garage_cars]
        prediction = PricePredictor(to_predict_list)
        print(prediction)
        return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()