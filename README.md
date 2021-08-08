<h1>MACHINE HACK HOUSE PRICE </h1>

####
[Download Dataset](https://www.kaggle.com/aquib5559/machine-hack-house-price) 
<p><h4>This dataset has been collected across various property aggregators across India.</h4></p>

## PROBLEM STATEMENT  <img src='https://img.shields.io/badge/Dataset-Kaggle-pink'>
<p>The objective of the dataset is to predict the house prices in India by designing an algorithm that will reflect the regression skills.</p>

## DISCOURSE 
Accurately predicting house prices can be a daunting task. The buyers are just not concerned about the size(square feet) of the house and there are various other factors that 
play a key role to decide the price of a house/property. 
It can be extremely difficult to figure out the right set of attributes that are contributing to understanding the buyer's behavior.
The dataset did not contain any NaN values fortunately.I have visualized the dataset and it has many outliers, I used scatterplots to get the idea of outliers. 
Then I scaled up all the features.This is a regression problem so I used Linear Regression, K-nearest neighbors(KNN), Decision Tree Regressor, Random Forest Regressor.
Out of these, I have found best R2 and RMSE in Random Forest Regressor model and then I used Cross Validation Score to find out the best model, and i found 
Random Forest Regressor to be the best among all the models on this dataset.



Below are the values of RMSE score , R2 score and Cross Validation score of the models based on the following algorithms:

````
 Linear Regression : 291.19558581607873, 0.762432494116685 and 0.7444613908795891
 K-Nearest Neighbours : 140.2954085199788, 0.94485522365451 and 0.9260903228575039
 Decision Tree Regressor : 150.06255219164254, 0.9369097685635955 and 0.9260995731919124
 Random Forest Regressor : 117.10073776712917, 0.961581825381928 and 0.9488189772063071
 ````
### Have a Look on some Visualizations

<img src = "Images/HEAT MAP.png">

<img src = "Images/SC PLOT 1.png">

<img src = "Images/SC PLOT 2.png">

## Prerequisites
 - Python
 - Pandas
 - Scikit Learn
 - FASTAPI
 - Uvicorn
 - A software to host your App.(e.g. heroku,DigitalOcean etc)


## Files
```
- main.py : This file contains all the routes
- schemas.py : Contains structure of model
- Model/House Price Prediction.ipynb : Jupyter Notebook with all the workings including visualization, pre-processing, modelling.
- Model/scale.pkl : Scaler object pickle file
- requirements.txt : pre-requisite libraries for the project
```
 
 
 ## FASTAPI
<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>FastAPI framework, high performance, easy to learn, fast to code, ready for production</em>

---

**Documentation**: <a href="https://fastapi.tiangolo.com" target="_blank">https://fastapi.tiangolo.com</a>

---

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.




### Interactive API docs

check this out >> <a href="https://know-your-houseprice.herokuapp.com/docs" class="external-link" target="_blank">https://know-your-houseprice.herokuapp.com/docs</a>.

You will see the automatic interactive API documentation (provided by <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>):

<img src = "Images/API 1.png">
</br>
<img src = "Images/API 2.png">

Here 0 means No and 1 means yes , e.g. If the property is RERA approved then write 1 otherwise 0 ,similiar inputs for the categorical columns.

### Deployment to Heroku 
Heroku is cloud service for hosting your applications. It is a Platform as a service with support for auto scaling and deployment. 
It primarily uses Git for deploying applications.
Refer to the documentation to see all the necessary commands : https://devcenter.heroku.com/


### Wanna Contribute?
- Clone/pull/download this repository.
- Create a virtualenv and install dependencies.
- Make relevant changes and Create Pull request

Comment your feedbacks, and do drop a ⭐ on the Github Repository.
