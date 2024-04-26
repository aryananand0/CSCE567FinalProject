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
st.title("Future Price Prediction")
st.write("The garph bellow predicts the future value of players and it does it because of the code. This code is like a smart calculator that learns from soccer player data to predict how much a player might be worth based on different characteristics like age, height, the league they play in, their playing position, and more. Imagine you're trying to guess the price of a house based on its size, location, and other features; this code does something similar but for soccer players' values.")
st.write("First, it gathers information about soccer players from a dataset, making sure all the data is ready and complete. Then, it starts to sort through this information to find patterns. For example, it looks at how a player's age or the league they play in might influence their value. It organizes this information into numbers that a computer can understand and uses a special technique called one-hot encoding to handle things like player nationality or the team they play for.")
st.write("Next, it takes a chunk of this data and hides it away, like a teacher hiding some questions to see if you've really learned. The rest of the data becomes like homework for our smart calculator, where it learns from the patterns and tries to predict the hidden part accurately. After a bit of studying, our calculator makes its best guesses about player values and checks how close it got to the real answers.")
residuals = y_test - predictions
fig_res = plt.figure(figsize=(10, 6))
plt.scatter(predictions, residuals, alpha=0.5)
plt.title('Residual Plot')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.axhline(y=0, color='r', linestyle='--', linewidth=2)
st.pyplot(fig_res)
st.write("The colorful graphs you see are like report cards for our calculator. The first one, called a residual plot, shows how well the calculator did in general—it's like checking how close the guesses were to the actual prices. The second graph compares the actual prices with what the calculator predicted, helping us see if it was generally accurate or made big mistakes.")
st.write("What this all means is that this code helps us understand what factors might make a soccer player more valuable and trains a computer to make educated guesses about player prices. It's like having a little assistant that learns from lots of examples and tries to make smart predictions, just like we do when we try to guess how much something is worth based on what we know.")

# Actual vs. Predicted plot
fig_pred, ax_pred = plt.subplots(figsize=(10, 6))
ax_pred.scatter(y_test, predictions, alpha=0.5)
ax_pred.set_title('Actual vs. Predicted Values')
ax_pred.set_xlabel('Actual Values')
ax_pred.set_ylabel('Predicted Values')
st.pyplot(fig_pred)
