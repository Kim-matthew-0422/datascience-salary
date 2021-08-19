# datascience-salary estimator:
* created tool that estimate data science salaries (mae)
* check each job description to find emphasis on different types of programs.
* scraped glassdoor (1000~)
* linear lasso, random forest regressions using gride searchCV
* client facing api using flask

# code and rss
* python 3.7
* packages: pandas, numpy, sklear, mapplotlib, seaborn, selenium, flask, json, pickle


# data cleaning
* salary into numeric data
* columns made for employer provided and hourly wages
* ratings
* company state parsing
* founded date into age of company
* types of programming used in description.

#EDA
below are few examples of pivot tables.

![alt text](https://github.com/Kim-matthew-0422/datascience-salary/blob/main/avgsalary.png "average salary")
![alt text](https://github.com/Kim-matthew-0422/datascience-salary/blob/main/location.png "location in US")
![alt text](https://github.com/Kim-matthew-0422/datascience-salary/blob/main/titlesalary.png "average salary for title")

# Model building

tried three different models and evaulated them using MAE.

* Multiple Linear Regression 
* Lasso Regression - due to spare data from many categorical variables
* Random Forest

# Model performance
Random forest far outperformed.
* Linear: 18.86k
* Lasso: 19.67k
* Random forest: 11.22k

#Productionization
Build a flask API endpoint hosted on local server, which akes requests with list of values from job listing and returns estimated salary.
