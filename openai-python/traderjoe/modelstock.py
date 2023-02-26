import sys
import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def predict_stock_price(symbol):
    # Load the historical stock price data from a local CSV file
    stock_data = pd.read_csv(symbol+".csv", parse_dates=['DATE'], index_col='DATE')

    # Keep only the rows with the specified symbol
    # stock_data = stock_data[stock_data['INTC'] == symbol]

    # Keep only the columns needed for predicting the stock price
    stock_data = stock_data[['OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME']]

    # Split the data into training and testing sets
    X = stock_data.drop(['CLOSE'], axis=1)
    y = stock_data['CLOSE']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the LightGBM model
    train_data = lgb.Dataset(X_train, label=y_train)
    test_data = lgb.Dataset(X_test, label=y_test)
    params = {'objective': 'regression', 'metric': 'rmse'}
    num_round = 100
    model = lgb.train(params, train_data, num_round, valid_sets=[test_data], early_stopping_rounds=5)

    # Make predictions on the test set
    y_pred = model.predict(X_test, num_iteration=model.best_iteration)

    # Calculate the root mean squared error of the predictions
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print('RMSE:', rmse)
    model.save_model(symbol+"_model.txt")

# Example usage:
# Usage : python modelstock.py INTC

if len(sys.argv) != 2:
    print("Usage : python modelstock.py <stock symbol>")
    sys.exit(1)

symbol = sys.argv[1]
predict_stock_price(symbol)

