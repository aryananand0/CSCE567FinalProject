import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import csv
from bokeh.plotting import figure
import altair as alt
import pydeck as pdk
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
 
def load_data():
    df = pd.read_csv('top5_leagues_player.csv')
    return df

Top_five_leagues_players=load_data()
Top_five_leagues_players = Top_five_leagues_players.fillna(method='bfill', axis=0).fillna(0)

# Define target and features
target = Top_five_leagues_players[['price']]
features = Top_five_leagues_players[['age', 'height', 'league','foot', 'position', 'club',
                        'contract_expires', 'joined_club', 'player_agent', 'outfitter', 'nationality']]

# Define columns to encode
columns_to_encode = ['league', 'foot', 'position', 'club', 'contract_expires', 'joined_club', 'player_agent', 'outfitter', 'nationality']

# Encode categorical columns
features.loc[:, columns_to_encode] = features.loc[:, columns_to_encode].astype(str)
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), columns_to_encode)], remainder='passthrough')
features_encoded = ct.fit_transform(features)

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(features_encoded, target, test_size=0.2, random_state=42)
y_train = y_train.values.ravel()
y_test = y_test.values.ravel()

model = LinearRegression()
model.fit(x_train, y_train)

# Make predictions
predictions = model.predict(x_test)

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions, squared=False)

# Residual plot
residuals = y_test - predictions
fig_res = plt.figure(figsize=(10, 6))
plt.scatter(predictions, residuals, alpha=0.5)
plt.title('Residual Plot')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.axhline(y=0, color='r', linestyle='--', linewidth=2)
st.pyplot(fig_res)

# Actual vs. Predicted plot
fig_pred, ax_pred = plt.subplots(figsize=(10, 6))
ax_pred.scatter(y_test, predictions, alpha=0.5)
ax_pred.set_title('Actual vs. Predicted Values')
ax_pred.set_xlabel('Actual Values')
ax_pred.set_ylabel('Predicted Values')
st.pyplot(fig_pred)