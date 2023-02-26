import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load data from local file
data_file = sys.argv[1] + ".csv"
data = pd.read_csv(data_file)
data = data.sort_values('DATE')

# Extract date and close price columns
dates = data['DATE'].values
close_price = data['CLOSE'].values

# Scale data between 0 and 1
scaler = MinMaxScaler(feature_range=(0, 1))
close_price = scaler.fit_transform(close_price.reshape(-1, 1))

# Split data into training and testing sets
train_size = int(len(close_price) * 0.8)
train_close_price = close_price[:train_size]
test_close_price = close_price[train_size:]

# Prepare training and testing data for LSTM model
def create_dataset(dataset, time_steps=1):
    X, Y = [], []
    for i in range(len(dataset)-time_steps):
        X.append(dataset[i:i+time_steps, 0])
        Y.append(dataset[i+time_steps, 0])
    return np.array(X), np.array(Y)

time_steps = 10

X_train, Y_train = create_dataset(train_close_price, time_steps)
X_test, Y_test = create_dataset(test_close_price, time_steps)

# Reshape data for LSTM input
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# Define LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(time_steps, 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

# Compile model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train model
model.fit(X_train, Y_train, epochs=50, batch_size=16)

# Evaluate model
test_loss = model.evaluate(X_test, Y_test)
print(f"Test loss: {test_loss}")

# Make predictions
test_predict = model.predict(X_test)
test_predict = scaler.inverse_transform(test_predict)
Y_test = scaler.inverse_transform([Y_test])

# Print predictions
for i in range(len(test_predict)):
    print(f"Predicted: {test_predict[i]}, Actual: {Y_test[0][i]}")

# Save model
model.save(sys.argv[1] + ".h5")

