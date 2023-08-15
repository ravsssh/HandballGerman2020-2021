import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import joblib
import tensorflow as tf
from tensorflow.keras.utils import register_keras_serializable
from tensorflow.keras import backend as K
from tensorflow.keras.layers import Dense, Flatten, Layer
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler
import numpy as np


@register_keras_serializable()
class RBFLayer(Layer):
    def __init__(self, units, gamma, **kwargs):
        super(RBFLayer, self).__init__(**kwargs)
        self.units = units
        self.gamma = gamma

    def build(self, input_shape):
        # Create a trainable weight variable for the centers of the RBFs
        self.centers = self.add_weight(name='centers',
                                      shape=(self.units, input_shape[-1]),
                                      initializer='uniform',
                                      trainable=True)
        super(RBFLayer, self).build(input_shape)

    def call(self, inputs):
        # Calculate the radial basis functions for each input sample and each RBF center
        diff = K.expand_dims(inputs) - self.centers  # shape: (batch_size, units, input_dim)
        norm = K.sum(K.square(diff), axis=-1)  # shape: (batch_size, units)
        rbf = K.exp(-self.gamma * norm)  # shape: (batch_size, units)

        return rbf

    def compute_output_shape(self, input_shape):
        return input_shape[0], self.units

model = tf.keras.models.load_model('model.keras', custom_objects={'RBFLayer': RBFLayer})
my_scaler = joblib.load('scaler.gz')

def make_prediction(input_values):
    scaled_input_values = my_scaler.transform(input_values)
    predictions = model.predict(scaled_input_values)
    return predictions
def main():
    st.title('Your Model Predictions')

    # Create input boxes for user input
    input_values = []
    for column_name in ["7MSHOT", "6MSHOT", "9MSHOT", "WINGSHOT", "PIVOTSHOT", "FASTBREAKSHOT"]:
        input_value = st.number_input(f"Enter {column_name}:", value=1.0)
        input_values.append(input_value)

    input_values = np.array([input_values])

    if st.button('Predict'):
        predictions = make_prediction(input_values)
        st.write('Predictions:')
        st.write(predictions)

if __name__ == '__main__':
    main()