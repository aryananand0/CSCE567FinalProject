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
position_counts = df['position'].value_counts().reset_index()
position_counts.columns = ['Position', 'Count']

# Create bar chart for position distribution with hover information
fig = px.bar(position_counts, x='Position', y='Count',
             title='Position Distribution of Players',
             hover_data={'Position': True, 'Count': True})

# Set axis labels
fig.update_xaxes(title_text='Position')
fig.update_yaxes(title_text='Count')

# Show plot with hover information
st.plotly_chart(fig)
