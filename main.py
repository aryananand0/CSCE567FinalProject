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


st.title("Exploring Player Profiles in Europe's Top Football Leagues")
 
def load_data():
    df = pd.read_csv('top5_leagues_player.csv')
    return df

df=load_data()
st.write("""
    In this comprehensive project, we delve into the visualization of various key aspects concerning players in the top 5 football/soccer leagues. Our exploration is centered around a rich dataset sourced from a CSV file named 'top5_leagues_player.csv'. Throughout this project, we aim to visualize and analyze a multitude of dimensions within the football landscape.

    Some of the focal points of our visualizations include:
    
    1. Price vs League: Examining the correlation between player prices and the leagues they belong to.
    2. Club vs Outfitter: Visualizing the relationship between football clubs and their respective outfitters.
    3. Age vs Price: Analyzing the relationship between player age and their market value.
    4. Position vs Price: Exploring how player positions impact their market values.
    5. Nation vs League: Exploring how nations are represented across different football leagues.
    6. Nation vs Market Value: Investigating the market values of players from different nations.
    7. Club Market Value: Analyzing the overall market value of football clubs.
    8. Left Foot vs Right Foot: Comparing the market values and distribution of left-footed and right-footed players.
    9. Future Market Value Predictor: Building a predictive model to forecast future market values of players.

    Through these visualizations and analyses, our overarching goal is to not only provide valuable insights into the football/soccer ecosystem but also to educate and inform enthusiasts about the intricacies and dynamics of this great sport.
    """)


st.write("## Scatter Plot from CSV")
st.write(df)





