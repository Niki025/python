# Import libraries
import tensorflow as tf
from tensorflow import keras

# Define model
model = keras.Sequential(
    [
        keras.layers.Dense(256, input_shape=(784,)),
        keras.layers.Activation("relu"),
        keras.layers.Dense(10),
    ]
)

# Compile model
model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

# Train model
model.fit(x_train, y_train, epochs=5)

# Make prediction
y_pred = model.predict(x_test)

print("AI model is ready!")
