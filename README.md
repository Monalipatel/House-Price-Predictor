# Final-Project

https://house-price-predictor7.herokuapp.com/

# Exoplanet Machine Learning Models

Create machine learning models to predict house prices.

## Table of contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Development Process](#development-process)
* [Resources](#resources)
* [Contact](#contact)

## General info

The objective of this project is to understand house price data through visualization. We first used Jupyter Notebook with Python and Pandas to clean and prepare the data set for machine learning. This first step also allows us to get a better understanding of the data which is helpful when we applied our machine learning code. Machine learning is used to predict house prices given the data set we used. We also developed an application that will predict a house's price given user inputs. This app was hosted on Hroku. 

## Technologies

### Language Used

* Python

### Data Extraction and Munging

* Jupyter notebook 
* Pandas
* Matplotlib
* seaborn

### Machine Learning

* scikit-learn - version 0.22.1

## Development Process

### Preprocess Data

We used a housing price dataset from a Kaggle machine learning competition. Initially, the data set contained > 80 columns, including: 
* Overall house quality
* Number of cars for garage
* Number of bedrooms and bathrooms
* House sale price ⇐ our target variable

#### Import Raw Data and Perform Basic Data Cleaning

* Drop the 5 columns with the most missing values
* Drop rows with missing values
* Remove “Id” column 
* Determine feature importance with a random forest regressor

#### Create Machine Learning Models

* We experimented with other models, including:
* Linear regression
* Lasso
* Ridge
* Elastic net
 However, they were less accurate than the random forest regressor.
 
 ### Random Forest Regressor
 
 Random Forest Regressor was the most accurate machine learning model for our data set. We achieved 85% accuracy.

##### Application

We created a flask app that predicts house prices based on user input.
* Load random forest regressor model using Joblib
* User input includes 8 features
* Predicted house price is 85% accurate

## Resources

* [Exoplanet Data Source](https://ww2.amstat.org/publications/jse/v19n3/decock/AmesHousing.txt)

## Contact

 Created by 
 
 Monali Patel 
 Shruti Jadhav 
 Pierce Henderson
