# Flight Price Predictor

## Overview
The Flight Price Predictor is a machine learning project designed to estimate the prices of domestic flights in India. This project leverages historical flight data scraped from EaseMyTrip.com for the period from February 11, 2022, to March 31, 2022. Users can input various parameters to receive a prediction of flight ticket prices, making it easier to anticipate and plan for travel expenses.

## Features
- Price Prediction: Input details such as date of departure, date of arrival, starting location, ending location, number of stops, and preferred airlines to get an estimated flight ticket price.
- Machine Learning Model: Utilizes the Logistic regression model for price prediction.
- Data Analysis: Involves data splitting into training and testing datasets, and analysis is performed on the training data.
- Visualization: Provides insights through performance graphs and model evaluation metrics.

## Tech Stack
- Programming Language: Python
- Libraries: Pandas, Numpy, Seaborn, Matplotlib, Scikit-Learn
- Modeling: Logistic Regression
- Environment: Jupyter Notebooks

## Installation
To get started with this project, clone the repository and install the required dependencies:
1. git clone https://github.com/lizatinku/Flight-Price-Predictor.git
2. cd Flight-Price-Predictor
3. pip install -r requirements.txt

## Usage
1. Prepare the Data: Ensure the dataset is correctly formatted and located in the specified directory.
2. Run the Jupyter Notebook: Open and run the Flight_Price_Predictor.ipynb notebook.
3. Input Parameters: Follow the instructions in the notebook to input the necessary parameters and receive flight price predictions.

## Example
Input parameters:
- Date of Departure: 2022-03-15
- Departure Time: 17:00
- Country Code: UK
- Starting Location: Delhi
- Ending Location: Mumbai
- Preferred Airline: Air India
### Output: Estimated Flight Price: ₹5,500

## Contributing
Feel free to submit pull requests or open issues for suggestions and improvements.
