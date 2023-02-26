import sys
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

import pandas as pd
import numpy as np

# Usage: python predict_lstm.py <symbol>
if len(sys.argv) != 2:
    print("Usage: python predict_lstm.py <symbol>")
    sys.exit(1)

symbol = sys.argv[1]
# Load saved model
model = load_model(symbol+".h5")

# Load new dataset
new_data = pd.read_csv(symbol + "_future.csv")
new_close_price = new_data['CLOSE'].values



scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(new_data)
# Scale new data between 0 and 1
new_close_price = scaler.transform(new_close_price.reshape(-1, 1))

# Prepare new data for LSTM model
X_new, Y_new = create_dataset(new_close_price, time_steps)
X_new = np.reshape(X_new, (X_new.shape[0], X_new.shape[1], 1))

# Make predictions on new data
new_predict = model.predict(X_new)

new_predict = scaler.inverse_transform(new_predict)

# Print predictions
print(new_predict)

