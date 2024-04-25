import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import csv
from bokeh.plotting import figure
import altair as alt
def load_data():
    df = pd.read_csv('top5_leagues_player.csv')
    return df
df=load_data()

st.title('Average Price by Position')

avg_prices = df.groupby('position')['price'].mean().reset_index()

# Display bar chart using Streamlit
st.bar_chart(avg_prices.set_index('position'))