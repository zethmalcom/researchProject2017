# Mining the HealthCare Data with Python
Used the Python programming language to create two programs that are able to parse through body.dat and riskfactors.csv data file in order to get

## Introduction
Data mining plays an important role in the healthcare industry to support today’s health systems in order to identify inefficiencies and best practices that improve care and reduce costs. These programs are focused on mining two sets of healthcare data from Center for Disease Control (CDC) and consists of two major parts: to analyze the correlation between Body Mass Index (BMI) and patient’s personal attributes, and to analyze five major risk factors closely related to the lifestyle and population heath in different states in US. Both parts employ the programming language Python to implement the data processing.

## Installation
For this project you need Python 3 installed on your workstation. Then you need to clone the repository to your local workstation.
```sh
https://github.com/zman322/data-mining-project
```
You need to download the body.dat and the riskfactors.csv data files given in the repository in order to mine the data.

## Description
The first program is the design and implementation of a BMI linear regression model with Python. BMI is the measure based on a person’s weight and height. This project uses a CDC dataset to identify a correlation with a person’s BMI and a combination of physical attributes such as weight, height and age. The least squares method has been implemented and applied and successfully established the correlation equation for data mining. The main part of this program is being able to decode the data, put the data into dictionaries, and then looping through the dictionaries in order to do the calculations needed for the slope, intercept, and coorelation.

The second program derives the so called “winnable Battle Risk factors and indicators”, the negative behaviors or health risks, from a CDC dataset. The indicators are identified include Heart Disease Death Rate, Motor Vehicle Death Rate, Teen Birth Rate, Adult Smoking, and Adult Obesity. The project successfully identifies the states in US with the best and worst records for each of these indicators. The main part of this program is knowing how to use the index of the max and min values you found by looping through the lists and using that to find the state that corresponds with the max and min data.

## Screenshots
Displays the output of the BMI Project.

<img width="555" alt="screen shot 2018-02-22 at 10 44 31 pm" src="https://user-images.githubusercontent.com/22325197/36578758-f05ec2cc-1824-11e8-995d-5347cbe2d6f3.png">

Displays the output of the Risk Factors Project.

<img width="698" alt="screen shot 2018-02-22 at 10 39 05 pm" src="https://user-images.githubusercontent.com/22325197/36578755-eed5250e-1824-11e8-87c5-5173b69679fe.png">
