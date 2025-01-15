# Importing the necessary libraries
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Title
st.title("Initial Cost Prediction for Franchise")

# Loading the dataset
data = pd.read_csv("data/slr12.csv", sep=";")

# Preparing the data
X = data[['FrqAnual']]  # Annual Frequency
y = data['CusInic']     # Initial Cost

# Training the model
model = LinearRegression().fit(X, y)

# Displaying data and plotting
col1, col2 = st.columns(2)

with col1:
    st.header("Data")
    st.table(data.head(10))  # Display the first 10 rows

with col2:
    st.header("Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(X, y, color='blue', label='Data Points')
    ax.plot(X, model.predict(X), color='red', label='Regression Line')
    ax.legend()
    st.pyplot(fig)

# User input for prediction
st.header("Annual Franchise Value:")
new_value = st.number_input("Enter New Value", min_value=1.0, max_value=999999.0, value=1500.0, step=0.01)
process = st.button("Process")

# Prediction
if process:
    new_data = pd.DataFrame([[new_value]], columns=['FrqAnual'])
    prediction = model.predict(new_data)
    st.header(f"Predicted Initial Cost: R$ {prediction[0]:.2f}")
