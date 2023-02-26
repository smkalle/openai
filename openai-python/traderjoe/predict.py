import pandas as pd
import numpy as np
import lightgbm as lgb
import sys
from sklearn.metrics import mean_squared_error

# Usage : python predict.py <stock symbol>
if len(sys.argv) != 2:
    print("Usage : python predict.py <stock symbol>")
    sys.exit(1)

# Load the data from CSV
symbol = sys.argv[1]
# df = pd.read_csv(f"{symbol}.csv", parse_dates=['DATE'])
df = pd.read_csv(f"{symbol}_future.csv", parse_dates=['DATE'])

# Prepare the data for training
train_data = df.iloc[:-6]
test_data = df.iloc[-6:]
X_train = train_data.drop(['DATE', 'CLOSE'], axis=1)
y_train = train_data['CLOSE']
X_test = test_data.drop(['DATE', 'CLOSE'], axis=1)

# Load the trained model
model = lgb.Booster(model_file=f"{symbol}_model.txt")

# Use the model to make predictions
y_pred = model.predict(X_test)

# Combine the predictions with the actual values
predictions = pd.DataFrame({'Date': test_data['DATE'], 'Actual': test_data['CLOSE'], 'Predicted': y_pred})

# Calculate the RMSE
rmse = np.sqrt(mean_squared_error(predictions['Actual'], predictions['Predicted']))
print(f"RMSE: {rmse}")

# Print the predictions
print(predictions)

